# GitHub Actions in this repository

This file explains what each workflow does, how the two preview workflows depend on each other, and how to check that a change to any of them actually works. Read it before editing anything in this directory.

The preview system broke twice in a row in 2026, both times silently, because these behaviors are not obvious from reading the YAML. The "Gotchas" section below is the short version if you are in a hurry.

## The workflows

| File                    | Name                       | Trigger                         | What it does                                                                                                                          |
| ----------------------- | -------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `build-preview.yml`     | Build Preview              | `pull_request`                  | Builds the site for a PR and uploads two artifacts: `preview-site` (the built site) and `pr-number` (the PR number). Deploys nothing. |
| `publish-preview.yml`   | Publish Preview Deployment | `workflow_run` on Build Preview | Downloads those artifacts, deploys to a Cloudflare Pages preview alias, and comments the URL on the PR.                               |
| `publish.yml`           | (unnamed)                  | `push` to `master`              | Builds and deploys the live site. Also opens an automatic PR if `find_missing_i18n_strings.py` changed `i18n/en.json`.                |
| `prettier.yml`          | autofix.ci                 | `pull_request`, `push`          | Runs `npx prettier --write .` and pushes formatting fixes back to the branch.                                                         |
| `update-checksums.yaml` | Update Checksums YAML      | schedule, every 4 hours         | Regenerates `data/get_almalinux_checksums.yaml` and opens or updates a PR when it changes.                                            |

## How the two preview workflows fit together

Preview deployment is deliberately split in two, because a PR from a fork should not be trusted with repository secrets.

1. **Build Preview** runs in the pull request's own context. For a fork PR, GitHub gives it a read-only token and no secrets, and the workflow narrows its own permissions to `contents: read` and `actions: read`. It builds the site and uploads it as an artifact. It does not deploy or write anything.
2. **Publish Preview Deployment** runs in the base repository's context, where the Cloudflare secrets exist. It takes the artifact the build produced and publishes it.

Everything fragile about this setup lives in the handoff between those two steps.

## Gotchas

Each of these has broken previews here. None of them surfaced an error when it did.

### `workflows:` matches the name, not the filename

The `workflow_run` trigger in `publish-preview.yml` refers to `"Build Preview"`, which is the `name:` field at the top of `build-preview.yml`. It is not the filename. The match is exact and case sensitive.

If you rename the Build Preview workflow, you must update the reference in `publish-preview.yml` in the same commit. A `workflow_run` trigger that matches nothing creates no run and logs no error. Nothing appears on the PR. The only symptom is that previews quietly stop, which is how this went unnoticed between August 4th and September 17th, 2026.

### `workflow_run` triggers are read from the default branch only

GitHub reads `workflow_run` trigger definitions from `master`, never from the PR branch. This means **a change to the `on:` block of `publish-preview.yml` cannot be tested on its own pull request.** The PR will build, show no preview, and tell you nothing about whether your change is correct. It only takes effect once merged.

Changes to the _steps_ of the job do run from the merged version too, for the same reason.

### Fork pull requests do not carry a PR number

In a `workflow_run` payload, `github.event.workflow_run.pull_requests[]` is populated only for pull requests opened from a branch in this repository. For a PR opened from a fork it is empty.

This is why `build-preview.yml` writes the number into a `pr-number` artifact and `publish-preview.yml` reads it back. The older approach of reading `pull_requests[0].number` directly produced an empty string on every fork PR, so each one deployed to the same `pr-` alias, overwriting the previous fork's preview, and the comment step returned early and reported success without commenting.

Because the build workflow runs from the pull request head, a fork controls the contents of that artifact. The "Resolve and verify PR number" step therefore checks that the number is numeric and that the head SHA of the PR it names matches the SHA this run actually built. Do not remove that check.

### The preview base URL is predicted, not read back

`build-preview.yml` builds with `--baseURL https://pr-<number>.<project>.pages.dev/` so that absolute links resolve against the preview rather than production. Without it, `og:image`, the canonical tag, the RSS feed, and every sitemap entry on a preview point at almalinux.org, which makes link previews impossible to check before merging.

The build cannot ask Cloudflare what the URL will be, because the deploy happens later, in a different workflow. It predicts it instead, and the prediction is only correct as long as `publish-preview.yml` keeps deploying with `--branch=pr-<number>`. **If you change that `--branch` value, change the formula in `build-preview.yml` in the same commit.** Nothing enforces this. A mismatch produces a preview whose pages all claim to live at a hostname that does not exist, and no step fails.

If `CLOUDFLARE_PROJECT_NAME` or the PR number is empty, the build falls back to the `baseURL` in `config.yaml` rather than assembling a broken hostname. A fork pull request that cannot read the variable therefore still builds, just with production URLs.

## Secrets and variables

| Name                      | Kind     | Used by                                                   |
| ------------------------- | -------- | --------------------------------------------------------- |
| `CLOUDFLARE_API_TOKEN`    | secret   | `publish.yml`, `publish-preview.yml`                      |
| `CLOUDFLARE_ACCOUNT_ID`   | variable | `publish.yml`, `publish-preview.yml`                      |
| `CLOUDFLARE_PROJECT_NAME` | variable | `publish.yml`, `publish-preview.yml`, `build-preview.yml` |

## Who can trigger what

The repository requires workflow approval for all external contributors, so a pull request from someone without write access sits at "action required" until a maintainer approves it. Nothing builds and nothing deploys before that click.

Once the build is approved and succeeds, the deploy runs automatically. There is no second approval. That is intentional: the maintainer's approval of the build is the trust decision, and the deploy publishes only to a per-PR preview alias, never to the live site.

An earlier design gated the deploy separately behind the `external` GitHub environment, which requires review from a named list of maintainers. That environment still exists but is no longer referenced by any workflow. It was removed because runs expire after 30 days if nobody approves them, and 262 preview runs across more than 40 branches expired that way before the change.

## Verifying a change before you merge it

Run these locally, from the repository root:

```bash
# Both files parse as YAML
node -e 'const fs=require("fs"),Y=require("yaml");for(const f of ["build-preview","publish-preview"].map(n=>`.github/workflows/${n}.yml`))console.log(f,JSON.stringify(Y.parse(fs.readFileSync(f,"utf8")).on??"ok"))'

# The workflow_run reference still matches the workflow name
diff <(grep -m1 '^name:' .github/workflows/build-preview.yml | sed 's/^name: *//') \
     <(grep -m1 'workflows: \[' .github/workflows/publish-preview.yml | sed 's/.*\["//;s/"\].*//') \
  && echo "name reference OK"

# Formatting matches what the pre-commit hook and autofix.ci expect
npx prettier --check .github/workflows/
```

After merging to `master`, confirm the change actually took effect. Push a small commit to any open pull request, ideally one from a fork, and check:

```bash
gh run list --workflow=build-preview.yml --limit 3
gh run list --workflow=publish-preview.yml --limit 3
```

You want a Publish Preview Deployment run that appeared within a minute or two of the Build Preview run finishing, and a comment on the PR with a `pr-<number>` URL.

Watch for these three failure signatures, all of which look like success at a glance:

- **No Publish Preview run at all.** The `workflow_run` trigger did not match. Check the workflow name reference.
- **A run where every step is green but no comment appeared.** A step returned early. Check the "Resolve and verify PR number" step output.
- **A deploy whose Cloudflare branch is `pr-` with no number.** The PR number did not survive the handoff. Check that `build-preview.yml` still uploads the `pr-number` artifact.

## Two oddities worth knowing

**`publish.yml` deletes the git directory before deploying.** The `rm -rf .git` step exists so that `wrangler` cannot infer a branch and falls back to a production deployment. It is a workaround for [cloudflare/pages-action#63](https://github.com/cloudflare/pages-action/issues/63). This is what "production" means in that file: the Cloudflare production environment, not a git branch. This repository does not appear to have a `production` branch.

**The repository default for `GITHUB_TOKEN` is write, with permission to approve pull request reviews.** Every workflow here narrows its own `permissions:` block, so this default does not currently matter, but anything new added to this directory should set its permissions explicitly rather than relying on the default being safe.

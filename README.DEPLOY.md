# Deployment

The live site deploys automatically from `master`. Any push to `master`, which in practice means a merged pull request, triggers `.github/workflows/publish.yml`, which builds the site with Hugo and publishes it to Cloudflare Pages.

Pull requests get their own preview deployment at a `pr-<number>` URL, posted as a comment on the PR. That is handled by a separate pair of workflows.

For what each workflow does, how the preview workflows depend on each other, and how to verify a change to any of them, see [.github/workflows/README.md](.github/workflows/README.md).

Cloudflare can add its own rules to the top of our robots.txt. It does this when Bot Preference Sync is turned on and an AI bot policy (such as Training) is set to Disallow, and the added block includes `Disallow` rules for AI crawlers and content signals such as `ai-train`. That would change what the site tells crawlers without a pull request, so leave Bot Preference Sync off for the almalinux.org zone and make robots.txt changes in `static/robots.txt`.

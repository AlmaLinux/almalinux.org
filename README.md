# almalinux.org website

[![almalinux.org](./screenshot.png)](https://almalinux.org)

This repository contains the source code for the AlmaLinux website at [https://almalinux.org](https://almalinux.org).

The site is built using the [Hugo](https://gohugo.io/) static site generator.

## Contributing

We welcome contributions for website updates, design improvements, and translations. Please follow the specific instructions provided for each contribution type:

- For blog content, see [Contributing - Blog Posts](https://github.com/AlmaLinux/almalinux.org/blob/main/contributing-blog-posts.md)
- For code or design improvements, see [Contributing - Code and Design](#contributing-code-and-design)
- For translations, see [Contributing - Translations](#localization-and-translation)

## Contributing - Code and Design

All development for the AlmaLinux website happens through this repository on GitHub.

### Reporting a Bug

Clear and detailed bug reports are incredibly valuable. A bug is a reproducible problem affecting the code or site functionality.

Please check the [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) to see if your issue has already been reported. A good bug report should include as many details as possible to avoid unnecessary follow-ups.

### Requesting a Feature

1. [Search existing issues](https://github.com/AlmaLinux/almalinux.org/issues) to see if the feature has already been requested. If so, give it a thumbs up or +1.
2. If no similar request exists, open a new issue. Please clearly explain why the feature is needed and provide a detailed use case.

### Contributing Code or Design Changes

Before submitting code changes, please check if there are any open issues or pull requests that cover your proposal. If not, open an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with a brief description and discuss it with the Marketing SIG first.

This helps avoid duplicated work and ensures proposed changes align with project goals.

For smaller contributions, follow this workflow:

- Create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) describing your changes.
- Await confirmation from contributors.
- Fork the project.
- Create a new branch for your feature or bug fix.
- Add your code, documentation, etc.
- Submit a pull request (PR). All PRs should target the `main` branch. Once approved, a development site will automatically generate based on the PR.

After review and approval, the changes will be merged into the `main` branch and deployed to the live site.

### For Developers

#### Local Development

To set up a local development environment, you need the following installed:

- Hugo

Run `hugo server` to start a near-production local development instance.

Localization is important! Please include proper localization formatting in your PR. After formatting, run `find_missing_i18n_strings.py` and `setup-pages-for-supported-languages.py`, then commit the changes. If you encounter issues with these scripts, please open an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with details.

#### Container Development

To use a container-based development environment, install Docker and use an editor supporting the devcontainer standard. Details can be found in the [README](.devcontainer/README.md).

#### Project Structure

- `/layouts/` — Hugo HTML templates
- `/layouts/partial` — Shared templates (header, footer, etc.)
- `/i18n/` — Localization and translation files
- `/static/` — Static files
- `/content/` — Markdown content for site pages
- `/data/` — Source data, currently only for the "Get AlmaLinux" page
- `config.yaml` — Hugo configuration
- `find_missing_i18n_strings.py` — Detects untranslated strings in `i18n/en.json`
- `setup-pages-for-supported-languages.py` — Creates placeholder markdown pages for missing languages

#### Updating 'Get AlmaLinux' page

The "Get AlmaLinux" page is dynamically generated using structured data and Hugo partial templates. This section explains how the data flows, which files are involved, and how to update the page for new releases or changes.

**How it works:**

- **Data sources:**
  - `data/get_almalinux_spec.yaml`: Defines available AlmaLinux versions, supported architectures, and the configuration for
    each section (e.g., ISO, Cloud, Container).
  - `data/get_almalinux_checksums.yaml`: Contains, for each version, the current highest point release (`fullVersion`) and the
    checksums for all artifacts (ISOs and cloud images) per architecture. This file can (and probably will) be generated.

- **Generation script:**
  - The script `tools/generate_get_almalinux_checksums.py` reads `data/get_almalinux_spec.yaml`, queries
    the CHECKSUM URLs defined for ISO and Cloud images, extracts the checksums and the current minor release
    and produces `data/get_almalinux_checksums.yaml`.
  - The script `tools/generate_get_almalinux_yaml.py` reads both YAML files, merges their data, and produces `data/get_almalinux.yaml`. This merged file is used by the Hugo partials to render the page.
  - `data/get_almalinux.yaml` is **not** tracked in git. It is generated automatically by the GitHub CI workflow during site builds, but you must run the script manually for local development if you change the source YAML files.

- **Templates:**
  - Hugo partials in `layouts/partials/get-almalinux/` render the page:
    - `tabs.html`: Renders version tabs and architecture dropdowns.
    - `tab-content.html`: Generates the content for each tab panel.
    - `arch-sections.html`: Generates the page for each version+architecture combination.
    - `section-*.html`: Renders each section (ISO, Cloud, Container, etc.) that makes up a full page.

##### Editing for a New Point Release

**In most cases, you only need to update `get_almalinux_checksums.yaml` when a new point release is available.**

1. Run the checksum generation script to update `get_almalinux_checksums.yaml` by looking at the source repos:
   ```bash
   python3 tools/generate_get_almalinux_checksums.py
   ```
2. Optionally, run the generation script to see your changes locally:
   ```bash
   python3 tools/generate_get_almalinux_yaml.py
   ```
   This updates `data/get_almalinux.yaml` for use by Hugo.
   This will be done automatically by the Gitlab CI scripts during deployment.
3. Commit the resulting changes to `data/get_almalinux_checksums.yaml` and open a PR.

##### Editing Sections, Architectures, or URL Patterns

If you need to change which sections or architectures are shown, or adjust how URLs are generated, edit `data/get_almalinux_spec.yaml`:

- The YAML file contains a `common` block, which sets default configuration for each section. These defaults are merged with per-version overrides in the `versions` array.
- Each version entry includes:
  - `id`: The major version (e.g., `10`, `10-kitten`).
  - `label`: The tab title.
  - `arches`: List of supported architectures (becomes dropdowns in the page).
  - `sections`: List of sections to configure for that version.
- Each section (such as `iso` or `cloud`) can inherit from `common` but may be overridden per version or architecture.
  - A section may have its own `arches` array to restrict it to certain architectures. For example, if cloud images for AlmaLinux 10 on `ppc64le` are not supported, the `cloud` section's `arches` array should exclude `ppc64le`.
  - To remove a section entirely for a version, omit it from the version's `sections` list.
  - To remove a specific cloud image within the `cloud` section, define it with no content (see the `oci` section in 10-kitten as an example).

##### URL Patterns and Variables

Most sections define URL templates for artifacts, using variables such as:

- `major`: The major version, from `id` (e.g., `10`, `10-kitten`).
- `full`: The full version, from `fullVersion` in `get_almalinux_checksums.yaml` (e.g., `10.1`). If `fullVersion` is not set, it falls back to `id`.
- `arch`: The architecture (e.g., `x86_64`, `x86_64_v2`).

Some URLs may allow other variables (like `variant`), or require different patterns per architecture (e.g., `vagrant`'s `registryUrls`). For advanced options, consult the code in `tools/generate_get_almalinux_yaml.py`.

##### Summary of Workflow

1. Edit `get_almalinux_checksums.yaml` for new point releases, or `get_almalinux_spec.yaml` for section/architecture changes.
2. Run the generation script to update the merged YAML:
   ```bash
   python3 tools/generate_get_almalinux_yaml.py
   ```
3. Start or restart the Hugo server to see your changes locally.

If you have questions about advanced configuration or variable support, refer to the script or open an issue for help.

### Localization and Translation

AlmaLinux.org translations are managed on [Weblate](https://hosted.weblate.org/engage/almalinux/). To contribute, join the [AlmaLinux project](https://hosted.weblate.org/projects/almalinux/) on Weblate. Submissions through Weblate generate automated PRs to this repo, which are reviewed and merged by the Marketing SIG or another team lead.

For translation guidelines, see [our Wiki](https://wiki.almalinux.org/Help-translating-site.html).

To request a new language, open an issue in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues).

[![Translation status](https://hosted.weblate.org/widget/almalinux/website-backend/multi-auto.svg)](https://hosted.weblate.org/engage/almalinux/)

### Change Approval Process

- Minor or cosmetic changes (typos, small style tweaks) can be reviewed and approved by any contributor with merge rights.
- Non-cosmetic changes require approval from the Marketing Lead.
- Weblate automatically submits PRs for translated strings; these are reviewed and merged by the Marketing SIG or team leads.

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

#### For Developers

##### Local Development

To set up a local development environment, you need the following installed:

- Hugo

Run `hugo server` to start a near-production local development instance.

Localization is important! Please include proper localization formatting in your PR. After formatting, run `find_missing_i18n_strings.py` and `setup-pages-for-supported-languages.py`, then commit the changes. If you encounter issues with these scripts, please open an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with details.

##### Container Development

To use a container-based development environment, install Docker and use an editor supporting the devcontainer standard. Details can be found in the [README](.devcontainer/README.md).

#### Project Structure

- `/layouts/` — Hugo HTML templates
- `/layouts/partial` — Shared templates (header, footer, etc.)
- `/i18n/` — Localization and translation files
- `/static/` — Static files
- `/content/` — Markdown content for site pages
- `config.yaml` — Hugo configuration
- `find_missing_i18n_strings.py` — Detects untranslated strings in `i18n/en.json`
- `setup-pages-for-supported-languages.py` — Creates placeholder markdown pages for missing languages

### Localization and Translation

AlmaLinux.org translations are managed on [Weblate](https://hosted.weblate.org/engage/almalinux/). To contribute, join the [AlmaLinux project](https://hosted.weblate.org/projects/almalinux/) on Weblate. Submissions through Weblate generate automated PRs to this repo, which are reviewed and merged by the Marketing SIG or another team lead.

For translation guidelines, see [our Wiki](https://wiki.almalinux.org/Help-translating-site.html).

To request a new language, open an issue in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues).

[![Translation status](https://hosted.weblate.org/widget/almalinux/website-backend/multi-auto.svg)](https://hosted.weblate.org/engage/almalinux/)

## Change Approval Process

- Minor or cosmetic changes (typos, small style tweaks) can be reviewed and approved by any contributor with merge rights.
- Non-cosmetic changes require approval from the Marketing Lead.
- Weblate automatically submits PRs for translated strings; these are reviewed and merged by the Marketing SIG or team leads.


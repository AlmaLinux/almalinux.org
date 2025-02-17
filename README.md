# almalinux.org website

[![almalinux.org](./screenshot.png)](https://almalinux.org)

This repository contains website source code for https://almalinux.org.

This website is built with the [Hugo](https://gohugo.io/) web framework.

## Contributing

We welcome contributions to the website in the form of website updates and design improvements, as well as translations. We've provided specific instructions on how to contribute for each part of the website. 

- Blog content, please see [Contributing - Blog Posts](https://github.com/AlmaLinux/almalinux.org/blob/master/contributing-blog-posts.md)
- Help with our Hugo implementation or design improvements, please see [Contributing - Code and Design](#contributing-code-and-design)
- To help with translations, please see [Contributing - Translations](#localization-and-translation)

## Contributing - Code and Design

All of the development of the AlmaLinux website is done through this repo on GitHub. 

### Reporting a Bug

Good bug reports can be very helpful. A bug is a demonstrable problem with the code or functionality.

Please use the [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues) and check if the issue has already been reported. A good bug report should be as detailed as possible, so that others won't have to follow up for the essential details. 

### Requesting a Feature

1. [Search the issues](https://github.com/AlmaLinux/almalinux.org/issues) for any open requests for the same feature, and give a thumbs up or +1 on existing requests.
1. If no previous requests exist, create a new issue. Please be as clear as possible about why the feature is needed and the intended use case.

### Contributing code or design edits

If you plan to propose code changes, please first confirm that there are no open issues or pull requests that match your proposal, and then open an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with a brief proposal and discuss it with the Marketing SIG first.

This is necessary to avoid more than one contributor working on the same feature/change and to avoid someone from spending time on feature/change that would not be merged for any reason.

For smaller contributions use this workflow:

* Create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) describing the changes.
* Await confirmation from contributors.
* Fork the project.
* Create a branch for your feature or bug fix.
* Add code changes, relevant documentation, etc.
* Send a pull request.  All PRs should be made against the `master` branch. Once your pull PR is approved, a dev site will be automatically created based on the PR. 

After one of the contributors has checked and approved the changes, they will be merged into master branch and will be automatically deployed to the live site.

#### For developers

To deploy local development environment, you will need following dependencies installed on your development host:

- hugo

Executing `hugo server` will deploy a nearly complete, ready to go local development environment.

Localization is important to us, and including localization formatting in your PR will be required. After you have formatted your text correctly, please run `find_missing_i18n_strings.py` and `setup-pages-for-supported-languages.py`, and then commit the changes to your branch. If you notice any issues with this script, please create an [issue](https://github.com/AlmaLinux/almalinux.org/issues) with details about the problem. 

#### Directories and modules

- `/layouts/` - Hugo HTML templates
- `/layouts/partial` - commonly used template such as header and footer
- `/i18n/` - Localization files and translations
- `/static/` - static files
- `/content/` - Markdown content for pages
- `config.yaml` - Hugo config
- `find_missing_i18n_strings.py` - find strings used in layouts/templates which do not exist in the base language file `i18n/en.json`
- `setup-pages-for-supported-languages.py` - create missing markdown pages for languages which do not exist. By default Hugo will return 404 for markdown content without localized pages. This script copies the English markdown to be served when translated copies are missing.

### Localization and translation

AlmaLinux.org localization and translation is managed using [Weblate](https://hosted.weblate.org/engage/almalinux/). To contribute translations join the [AlmaLinux](https://hosted.weblate.org/projects/almalinux/) localization project in Weblate. Translations submitted through Weblate are automatically submitted to this repo as a pull request. Those pull requests are then reviewed by a member of the marketing SIG or another team lead, and merged as appropriate. To help with translations, please see [Contributing - Translations](#localization-and-translation).

You can request new languages to be added by creating a ticket in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues).

[![Translation status](https://hosted.weblate.org/widget/almalinux/website-backend/multi-auto.svg)](https://hosted.weblate.org/engage/almalinux/)

## Approval of changes

Before any changes can be merged:

- All minor or cosmetic changes (typos, minor styling, etc) can be reviewed and approved by any contributor with merge rights
- All non-cosmetic changes to the website requires the approval of the Marketing lead
- Weblate automatically creates pull requests with new translated strings. Those pull requests are then reviewed by a member of the marketing SIG or another team lead, and merged as appropriate.

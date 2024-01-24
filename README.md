# almalinux.org website

[![almalinux.org](./screenshot.png)](https://almalinux.org)

This repository contains website source code for https://almalinux.org.

This website is built with the [Hugo](https://gohugo.io/) web framework.

## For developers

To deploy local development environment, you will need following dependencies installed
on your development host:

- hugo

Executing `hugo server` will deploy a nearly complete, ready to go development environment.

Localization will be incomplete unless you first run `find_missing_i18n_strings.py` and
`setup-pages-for-supported-languages.py`.  Please do **not** commit the files which are output by these scripts.

### Directories and modules

- `/layouts/` - Hugo HTML templates
- `/layouts/partial` - commonly used template such as header and footer
- `/i18n/` - Localization files and translations
- `/static/` - static files
- `/content/` - Markdown content for pages
- `config.yaml` - Hugo config
- `find_missing_i18n_strings.py` - find strings used in layouts/templates which do not exist in the base language file
  `i18n/en.json`
- `setup-pages-for-supported-languages.py` - create missing markdown pages for languages which do not exist.
  By default Hugo will return 404 for markdown content without localized pages.  This script copies the English
  markdown to be served when translated copies are missing.

### Localization and translation

AlmaLinux OS localization and translation is managed using [Weblate](https://hosted.weblate.org/engage/almalinux/).

To contribute translations see [AlmaLinux OS](https://hosted.weblate.org/projects/almalinux/) localization project in Weblate.

You can request new languages to be added by creating a ticket in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues).

[![Translation status](https://hosted.weblate.org/widgets/almalinux/-/287x66-white.png)](https://hosted.weblate.org/engage/almalinux/)

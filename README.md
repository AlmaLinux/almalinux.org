# almalinux.org website

[![almalinux.org](./screenshot.png)](https://almalinux.org)

This repository contains website source code for future https://almalinux.org.

This website is built with Python using Django web framework. It uses MariaDB as database backend,
Docker and docker-compose for development environment deployment, and Pipenv is used to track project 
requirements, and manage Python dependencies.

JavaScript and SCSS is used for frontend, and is managed/built using Webpack Encore. See
[frontend/README](./frontend/README.md) for more details.

## For developers

To deploy local development environment, you will need following dependencies installed
on your development host:

- Docker
- docker-compose
- make

Common development commands and automation related commands are listed in Makefile. Execute `make help`
for a complete list of available commands.

Executing `make dev` will deploy a complete, ready to go development environment.

### Directories and modules

- `/almalinux/` - Django project root.
- `/commons/` - A Django app-module with reusable utilities for app support.
- `/locale/` - Django locale files.
- `/media/` - Django file uploads.
- `/static/` - Static files and build output for frontend code.
- `/www/` - Django app that contains all logic for the website.
- `/frontend/` - JavaScript and SCSS frontend code.

### Localization and translation

AlmaLinux OS localization and translation is managed using [Weblate](https://hosted.weblate.org/engage/almalinux/).

To contribute translations see [AlmaLinux OS](https://hosted.weblate.org/projects/almalinux/) localization project in Weblate.

You can request new languages to be added by creating a ticket in [GitHub issues](https://github.com/AlmaLinux/almalinux.org/issues).

[![Translation status](https://hosted.weblate.org/widgets/almalinux/-/287x66-white.png)](https://hosted.weblate.org/engage/almalinux/)

Copyright (c) 2021 AlmaLinux OS Foundation

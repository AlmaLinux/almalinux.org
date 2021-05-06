# almalinux.org website

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


Copyright (c) 2021 AlmaLinux OS Foundation

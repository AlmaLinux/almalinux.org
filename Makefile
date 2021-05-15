ROOT_DIR		:= $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
CURRENT_UID 	:= $(shell id -u)
CURRENT_GID 	:= $(shell id -g)

.PHONY:		default
default:	dev ;

dev: #: Start development environment
	cp -n .env.dist .env
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose up --abort-on-container-exit

build-dev: #: Build development Docker images
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose build web
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose build frontend

clean-dev: #: Clean development environment, remove docker images and data
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose down --rmi local -v

mypy: #: Run mypy static type checker for Python modules
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run -u ${CURRENT_UID} web pipenv run mypy almalinux www commons

web-shell: #: Enter backend shell within docker, as a regular user, new service instance
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run -u ${CURRENT_UID} web /bin/bash

web-root-shell: #: Enter backend shell within docker, as root, new service instance
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run web /bin/bash

web-attach: #: Attach to backend shell within docker, as a regular user, running instance
	docker exec -ti -u ${CURRENT_UID} web /bin/bash

web-root-attach: #: Attach to backend shell within docker, as root, running instance
	docker exec -ti web /bin/bash

frontend-shell: #: Enter frontend shell within docker, as a regular user, new service instance
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run -u ${CURRENT_UID} frontend /bin/bash

frontend-root-shell: #: Enter frontend shell within docker, as root, new service instance
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run frontend /bin/bash

frontend-attach: #: Attach to frontend shell within docker, as a regular user, running instance
	docker exec -ti -u ${CURRENT_UID} frontend /bin/bash

frontend-root-attach: #: Attach to frontend shell within docker, as root, running instance
	docker exec -ti frontend /bin/bash

runserver: # INTERNAL - start internal development server. This is supposed to be run inside Docker.
	@echo 'Delaying start of local development server to allow for dependencies to boot'
	@sleep 5
	su - web -c 'cd /app && pipenv install --dev'
	su - web -c 'cd /app && pipenv run python3 manage.py migrate'
	su - web -c 'cd /app && pipenv run python3 manage.py runserver 0.0.0.0:8080'

frontend-runserver: # INTERNAL - start internal frontend development server. This is supposed to be run inside Docker.
	su - web -c 'yarn --cwd=/app/frontend/ install'
	su - web -c 'yarn --cwd=/app/frontend/ dev-server --host 0.0.0.0 --public http://localhost:8090 --port 8090'

help: #: Show this help
	@fgrep -h "#:" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/#://'

all: dev

%:
	@echo 'Invalid command'
	@make help

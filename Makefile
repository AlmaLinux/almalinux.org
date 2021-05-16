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

assemble: # INTERNAL: assemble deployment asset for deployment
	rm -rf tmp/deploy
	rm -rf tmp/deploy_out
	mkdir -p tmp
	mkdir -p tmp/deploy_out
	git clone git@github.com:AlmaLinux/almalinux.org.git tmp/deploy
	# Use local install .venv and node_modules to reuse local install as sort of a cache
	cp -R .venv tmp/deploy
	cp -R frontend/node_modules tmp/deploy/frontend
	# Build dependencies
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run -u ${CURRENT_UID} frontend /bin/bash -c 'cd /app/tmp/deploy/ && make assemble-frontend'
	LOCAL_UID=${CURRENT_UID} LOCAL_GID=${CURRENT_GID} docker-compose run -u ${CURRENT_UID} web /bin/bash -c 'cd /app/tmp/deploy/ && make assemble-web'
	# Cleanup
	rm tmp/deploy/Pipfile
	rm tmp/deploy/Pipfile.lock
	rm tmp/deploy/.env
	rm tmp/deploy/.env.dist
	rm -rf tmp/deploy/.git
	rm -rf tmp/deploy/.venv
	rm -rf tmp/deploy/static
	rm -rf tmp/deploy/media
	rm -rf tmp/deploy/Dockerfile*
	rm -rf tmp/deploy/docker-compose.yml
	rm -rf tmp/deploy/.mypy.ini
	rm -rf tmp/deploy/.editorconfig
	rm -rf tmp/deploy/.gitignore
	rm -rf tmp/deploy/README.md
	rm -rf tmp/deploy/CONTRIBUTING.md
	rm -rf tmp/deploy/screenshot.png
	# Build production docker image
	docker build --rm -f ./Dockerfile-production -t almalinux.org:latest .
	# Exporting image for deployment...
	docker save almalinux.org:latest > tmp/deploy_out/almalinux.org.image.tar
	# Assembling deployment asset
	mv tmp/deploy/public tmp/deploy_out
	cp tmp/deploy/docker-compose.production.yml tmp/deploy_out/docker-compose.yml
	cd tmp/deploy_out && tar -zcvf ../deployment.tar.gz .
	# Cleanup deployment workspace
	rm -rf tmp/deploy_out/
	rm -rf tmp/deploy/

assemble-frontend: # INTERNAL - package and build frontend
	yarn --cwd=/app/tmp/deploy/frontend/ install
	yarn --cwd=/app/tmp/deploy/frontend/ build
	rm -rf /app/tmp/deploy/frontend

assemble-web: # INTERNAL - package and build web
	cp /app/tmp/deploy/.env.dist /app/tmp/deploy/.env
	cd /app/tmp/deploy/ && pipenv sync
	cd /app/tmp/deploy/ && pipenv clean
	cd /app/tmp/deploy/ && pipenv run ./manage.py collectstatic
	cd /app/tmp/deploy/ && pipenv run ./manage.py compilemessages
	cd /app/tmp/deploy/ && pipenv lock -r > requirements.txt

uwsgi: # INTERNAL - start UWSGI server, within production image
	uwsgi \
		--chdir=/app/ \
		--module=almalinux.wsgi:application \
		--master \
		--pidfile=/tmp/almalinux.org.pid \
		--socket=0.0.0.0:9000 \
		--processes=4 \
		--enable-threads \
		--threads=2 \
		--harakiri=20 \
		--max-requests=5000 \
		--vacuum

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

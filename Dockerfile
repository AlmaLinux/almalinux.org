# Docker image for local development environment.
# You should NOT publish this image, it is intended for local use only.

FROM almalinux/almalinux:8

ARG LOCAL_UID
ARG LOCAL_GID

RUN groupadd -g ${LOCAL_GID} web && \
    useradd -ms /bin/bash web -g ${LOCAL_GID} -u ${LOCAL_UID}

RUN dnf -y install \
    gcc \
    make \
    gettext \
    python38 \
    python38-devel \
    mariadb-devel

RUN pip3 install pipenv

# Work around IDEA remote interpreter not able to work with remote virtualenvs
RUN touch /root/.bashrc \
    && echo 'if [[ -f "/app/.venv/bin/activate" ]]; then source /app/.venv/bin/activate; fi' >> /root/.bashrc

RUN touch /home/web/.bashrc \
    && echo 'if [[ -f "/app/.venv/bin/activate" ]]; then source /app/.venv/bin/activate; fi' >> /home/web/.bashrc

WORKDIR /app

CMD make runserver

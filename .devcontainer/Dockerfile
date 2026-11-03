# Use AlmaLinux as the base image
FROM almalinux:latest

# Update and install necessary packages
RUN dnf update -y && \
    dnf install -y \
    git \
    python3 \
    python3-pyyaml \
    nodejs24 \
    nodejs24-npm \
    shadow-utils \
    sudo \
    && dnf clean all \
    && for bin in node npm npx; do ln -s /usr/bin/$bin-24 /usr/local/bin/$bin; done

ARG WORKSPACE_DIR

# Install Hugo and Dart Sass at the versions pinned in package.json
COPY package.json package-lock.json /opt/site-tools/
RUN cd /opt/site-tools && HUSKY=0 npm ci && npm cache clean --force
ENV PATH="/opt/site-tools/node_modules/.bin:${PATH}"

# Create a non-root user for development
ARG USERNAME=alma_www_user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER alma_www_user

# Expose port for Hugo server
EXPOSE 1313

# Set the working directory to the container workspace directory
WORKDIR ${WORKSPACE_DIR}

ENTRYPOINT ["hugo", "server"]
CMD ["--bind=0.0.0.0", "--buildFuture", "--poll=700ms"]

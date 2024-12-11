# Use AlmaLinux as the base image
FROM almalinux:latest

# Update and install necessary packages
RUN dnf update -y && \
    dnf install -y \
    git \
    python3 \
    python3-pyyaml \
    wget \
    tar \
    shadow-utils \
    sudo \
    && dnf clean all

# Set up arguments for Hugo installation
ARG HUGO_VERSION=latest
ARG HUGO_VARIANT=hugo_extended
ARG WORKSPACE_DIR

# Download and install Hugo
RUN if [ "$HUGO_VERSION" = "latest" ]; then \
    HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep "tag_name" | awk '{print substr($2, 3, length($2)-4)}'); \
    fi && \
    ARCH=$(uname -m) && \
    case "$ARCH" in \
    "x86_64") HUGO_ARCH="64bit";; \
    "arm64"|"aarch64") HUGO_ARCH="arm64";; \
    *) echo "Unsupported architecture: $ARCH" && exit 1;; \
    esac && \
    echo "Installing Hugo version: ${HUGO_VERSION}" && \
    wget -O hugo.tar.gz https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_VARIANT}_${HUGO_VERSION}_Linux-${HUGO_ARCH}.tar.gz && \
    tar -xzf hugo.tar.gz && \
    mv hugo /usr/local/bin/hugo && \
    chmod +x /usr/local/bin/hugo && \
    rm hugo.tar.gz

# Create a non-root user for development
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER vscode

# Expose port for Hugo server
EXPOSE 1313

# Set the working directory to the container workspace directory
WORKDIR ${WORKSPACE_DIR}

# Set the default command to run Hugo server
CMD ["hugo", "server", "--bind=0.0.0.0"]
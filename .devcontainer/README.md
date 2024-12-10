### Devcontainer Features:

- VSCode Extensions: Automatically installs the following extensions for optimal Hugo development:
  _budparr.language-hugo-vscode - Hugo syntax support
  ms-python.python - Python development support
  esbenp.prettier-vscode - Code formatting
  yzhang.markdown-all-in-one - Enhanced Markdown editing
  tamasfe.even-better-toml - TOML language support_

- **Terminal Configuration:** Sets the integrated terminal to /bin/bash for a familiar shell experience.
- **Port Forwarding:** Configures port 1313 to be forwarded for Hugo's live server.
- **User Configuration:** Sets remoteUser to vscode, providing a secure, non-root user environment.

### Dockerfile Setup:

- **Base Image:** Utilizes the latest AlmaLinux image for compatibility and security.
- **System Updates:** Ensures all system packages are up-to-date.
- **Software Installation:** Includes essential tools like git, python3, python3-pyyaml, wget, tar, shadow-utils, and sudo.
- **Hugo Installation:** Fetches and installs the latest Hugo extended binary for dynamic site generation.
- **User Management:** Creates and configures a vscode user with sudo privileges to enhance security and usability.
- **Port Exposure:** Exposes port 1313 to allow Hugo's development server to be accessed externally.

This setup aims to streamline the development process by automating the environment setup, ensuring consistency across different machines, and reducing the time spent on configuration. Please review and provide feedback or approval to merge.

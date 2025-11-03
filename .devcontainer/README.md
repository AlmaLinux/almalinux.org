# Devcontainer Features

## VSCode Extensions

Automatically installs the following extensions for optimal Hugo development:

- `budparr.language-hugo-vscode` - Provides syntax highlighting and IntelliSense for Hugo templates.
- `ms-python.python` - Enhances Python development with features like debugging and testing.
- `esbenp.prettier-vscode` - Formats code according to Prettier rules for consistency.
- `yzhang.markdown-all-in-one` - Offers advanced Markdown editing capabilities.
- `tamasfe.even-better-toml` - Adds support for TOML files, which are often used in Hugo configurations.
- `ms-azuretools.vscode-docker` - Integrates Docker functionality for container management.

- **Terminal Configuration:** Sets the integrated terminal to `/bin/bash` for a familiar shell experience.
- **Port Forwarding:** Configures port 1313 to be forwarded for Hugo's live server.
- **User Configuration:** Sets `remoteUser` to `alma_www_user`, providing a secure, non-root user environment.

## Dockerfile Setup

- **Base Image:** Utilizes the latest AlmaLinux image for compatibility and security.
- **System Updates:** Ensures all system packages are up-to-date.
- **Software Installation:** Includes essential tools like `git`, `python3`, `python3-pyyaml`, `wget`, `tar`, `shadow-utils`, and `sudo`.
- **Hugo Installation:** Fetches and installs Hugo with dynamic version support:
  - If `VERSION` is set to `latest`, it downloads the latest Hugo extended binary.
  - If a specific version is provided e.g. `v0.139.1`, it downloads and installs that version. This can be specified in `devcontainer.json` under `build.args`.

- **User Management:** Creates and configures an `alma_www_user` with sudo privileges to enhance security and usability.
- **Port Exposure:** Exposes port 1313 to allow Hugo's development server to be accessed externally.
- **Working Directory:** Sets the working directory to the specified `WORKSPACE_DIR`.

## Accessing the Live Server

**Starting the Server:** Upon opening the project in the container, Hugo's live server automatically starts. You can access it by navigating to `http://localhost:1313` in your web browser. This server runs in the background, allowing for real-time testing of your Hugo site.

**Editing and Hot Rebuild:**

- **Editing Files:** You can edit project files directly within your devcontainer supported editor of choice as the container mounts your local project directory, changes are reflected in real-time. This setup is not limited to VS Code; any editor that supports devcontainers will work.

- **Hot Rebuild:** Hugo's live server supports hot reloading. This means that when **changed** files are **saved**, Hugo automatically rebuilds the site, and the changes are immediately reflected in the live server. There's no need to manually restart the live server; just save your edits, and refresh your browser to see the updated site. Note that while hot reloading provides quick updates, it might slightly increase build times or resource usage depending on the complexity of your site.

## Troubleshooting

- **Docker Not Running:** Ensure Docker is installed and running on your machine before opening the project in a devcontainer.
- **Connection Issues:** If `localhost:1313` doesn't work, check your port forwarding settings or ensure no other service is using port 1313.

For more detailed information on Hugo's live server and hot reloading, refer to the [Hugo documentation](https://gohugo.io/getting-started/usage/#livereload).

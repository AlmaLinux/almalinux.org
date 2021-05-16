# Deployment

The website is currently designed to run on a single host.

## Preparing a host

- Go to `ansible/` and apply all relevant roles to the new host.
- Create `.env` file in `/opt/almalinux.org/` directory on the target host.
- Deploy!

## Deploying

Execute `kafe do <staging|production> deploy`. This will build from master and deploy to the target environment.

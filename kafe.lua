-- See https://github.com/libkafe/kafe for documentation.

local k = require('kafe')
k.require_api(1)

k.add_inventory('deploy', '159.65.52.14', 22, 'staging', 'website')

k.task('deploy', function()
    local version = os.time(os.date('!*t'))

    k.define('deploy_to', '/opt/almalinux.org')
    k.define('public', '/var/www/almalinux.org')
    k.define('version', version)

    k.local_shell('make assemble')

    local deploy = function()
        k.within('{{deploy_to}}')

        if not k.shell('mkdir -p release/{{version}}')
            then error('Could not create release root directory') end

        k.upload_file('tmp/deployment.tar.gz', 'release/{{version}}/deployment.tar.gz')

        if not k.shell('tar -xf release/{{version}}/deployment.tar.gz -C release/{{version}}')
            then error('Could not unpack uploaded archive') end

        if not k.shell('rm release/{{version}}/deployment.tar.gz')
            then error('Failed to remove uploaded archive') end

        k.shell('docker load < release/{{version}}/almalinux.org.image.tar')
        k.shell('cp release/{{version}}/docker-compose.yml docker-compose.yml')
        k.shell('mkdir -p {{public}}/release/{{version}}')
        k.shell('mv release/{{version}}/public {{public}}/release/{{version}}')
        k.shell('/usr/local/bin/docker-compose up -d mariadb && sleep 5')
        k.shell('/usr/local/bin/docker-compose run web python3 ./manage.py migrate')
        k.shell('/usr/local/bin/docker-compose up -d web')
        k.shell('docker system prune -f')
    end

    local symlink_www = function()
        k.within('{{public}}')

        if not k.shell('ln -nsfv release/{{version}}/ current')
            then error('Failed to update the symlink to the new version') end
    end

    local remove_old_public_releases = function()
        k.within('{{public}}/release/')

        if not k.shell('ls -1tr | head -n -3 | xargs -d \'\\n\' rm -rf --') then
            error('Failed to remove old www releases') end
    end

    local remove_old_app_releases = function()
        k.within('{{deploy_to}}/release/')

        if not k.shell('ls -1tr | head -n -3 | xargs -d \'\\n\' rm -rf --') then
            error('Failed to remove old app releases') end
    end

    if k.on('website', deploy) then
        k.on('website', symlink_www)
        k.on('website', remove_old_public_releases)
        k.on('website', remove_old_app_releases)
    end
end)

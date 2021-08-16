const path = require('path');
const Encore = require('@symfony/webpack-encore');

if (!Encore.isRuntimeEnvironmentConfigured()) {
    Encore.configureRuntimeEnvironment(process.env.NODE_ENV || 'dev');
}

if (Encore.isProduction()) {
    process.env.NODE_ENV = 'production';
}

const BUILD_DIR = path.resolve(__dirname + '/../static/build/')

Encore
    .setOutputPath(BUILD_DIR)
    .setPublicPath('/static/build')
    .splitEntryChunks()
    .enableSingleRuntimeChunk()
    .cleanupOutputBeforeBuild()
    .enablePostCssLoader()
    .enableSourceMaps(!Encore.isProduction())
    .enableVersioning(Encore.isProduction())
    .configureBabelPresetEnv((config) => {
        config.useBuiltIns = 'usage';
        config.corejs = 3;
    })
    .enableSassLoader()
    .configureDevServerOptions((config) => {
        config.static = false;
    })

    // Common CSS and JavaScript for the whole website
    .addEntry('common', __dirname + '/src/common/js/main.js')
    .addEntry('admin', __dirname + '/src/admin/js/main.js')
    // Page modules
    .addEntry('page_index', __dirname + '/src/modules/page_index/main.js')
    .addEntry('page_page', __dirname + '/src/modules/page_page/main.js')
    .addEntry('page_blog', __dirname + '/src/modules/page_blog/main.js')
    .addEntry('page_showcase', __dirname + '/src/modules/page_showcase/main.js')
    .addEntry('page_contribute', __dirname + '/src/modules/page_contribute/main.js')
    .addEntry('page_foundation', __dirname + '/src/modules/page_foundation/main.js')
;

if (Encore.isDevServer() || Encore.isDev()) {
    Encore.disableCssExtraction();
}

Encore.addAliases({
    '@common': path.resolve(__dirname, 'src/common/'),
    '@modules': path.resolve(__dirname, 'src/modules/'),
    '~static': path.resolve(__dirname, '../static/'),
})

module.exports = Encore.getWebpackConfig();

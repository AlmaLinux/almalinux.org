const path = require('path');
const Encore = require('@symfony/webpack-encore');

if (!Encore.isRuntimeEnvironmentConfigured()) {
  Encore.configureRuntimeEnvironment(process.env.NODE_ENV || 'dev');
}

if (Encore.isProduction()) {
  process.env.NODE_ENV = 'production';
}

const BUILD_DIR = path.normalize(__dirname + '/../static/build/')

Encore
  .setOutputPath(BUILD_DIR)
  .setPublicPath('/static/build')
  .splitEntryChunks()
  .enableSingleRuntimeChunk()
  .cleanupOutputBeforeBuild()
  .enablePostCssLoader()
  .enableSourceMaps(!Encore.isProduction())
  .enableVersioning(Encore.isProduction())
  .configureBabel((config) => {
  })
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
;

if (Encore.isDevServer() || Encore.isDev()) {
  Encore.disableCssExtraction();
}

Encore.addAliases({
  '@common': path.resolve(__dirname, 'src/common/'),
  '@modules': path.resolve(__dirname, 'src/modules/')
})

module.exports = Encore.getWebpackConfig();

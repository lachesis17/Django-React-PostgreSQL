const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
    clean: true  // Ensures that the build folder is cleaned between builds
  },
  devServer: {
    static: './build',
    port: 3000  // Defines the port the dev server will run on
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|ico)$/,
        type: 'asset/resource'
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',
      favicon: './public/favicon.ico'  // Adding favicon through HtmlWebpackPlugin
    }),
    new CopyPlugin({
      patterns: [
        { from: 'public/gitLogo.png', to: 'gitLogo.png' },
        { from: 'public/logo192.png', to: 'logo192.png' },
        { from: 'public/logo512.png', to: 'logo512.png' },
        { from: 'public/manifest.json', to: 'manifest.json' },
        { from: 'public/robots.txt', to: 'robots.txt' },
        { from: 'build', to: path.resolve(__dirname, '../djangoUnchained/core/static/build') }
      ]
    })
  ],
  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },
  externals: {
    'react': 'React',
    'react-dom': 'ReactDOM',
  }
};

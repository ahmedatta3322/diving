module.exports = {
  entry: {
    main: "./frontend/src/index.js",
    register: "./frontend/src/register.js",
    create: "./frontend/src/create.js",
    view: "./frontend/src/view.js"


  }
  ,
  output: {
    filename: "[name].js",
    path: __dirname + '/frontend/static/frontend/'
  },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        }
      ]
    }

  };
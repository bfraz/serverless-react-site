# Serverless React Website


## Installing from ubuntu server

```
sudo apt-get update
sudo apt-get -y install nodejs npm
sudo apt-get -y install openjdk-8-jdk
sudo apt install -y unzip
git clone https://github.com/bfraz/serverless-react-site.git
cd serverless-react-site
npm install
npm install -g local-web-server
npm run webpack-dev
ws
```


Expect the site to be on port 8000. Either try public ip of server or localhost depending on your setup.


## Notes starting from scratch
```
npm init
npm install --save react@16.2.0 react-dom@16.2.0
npm install --save-dev webpack@4.2.0 webpack-cli@2.0.13
npm install --save-dev babel-core@6.26.0 babel-loader@7.1.4 babel-preset-react@6.24.1
npm install --save-dev babel-jest@22.4.3 enzyme@3.3.0 jest@22.4.3 babel-preset-env@1.6.1 enzyme-adapter-react-16@1.1.1 react-test-renderer@16.2.0
```

## Local startup, assuming env is set up and code has been cloned

```
npm install
npm test
npm run webpack-dev
ws
```

# To run tests

```npm test```



#### Influenced by acloud.guru Serverless Portfolio course

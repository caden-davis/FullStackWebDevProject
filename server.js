// File to start both APIs, used for npm script

var tsAPI = require('./TorchServeAPI/tsServer'),
    dbAPI = require('./DatabaseAPI/apiServer');

tsAPI();
dbAPI();
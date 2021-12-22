// Basic App Setup
var express = require('express'),
    app = express(),
    port = process.env.PORT || 3002;

// Start the App
app.listen(port);
console.log("TorchServeAPI started successfully on port " + port);

// Express -- GET --> JS Child Process -- SPAWN --> Python
// Python Handler -- STDOUT --> API res
app.get('/ts', function(req, res) {
    var spawn = require('child_process').spawn;
    var process = spawn('python', ['tsHandler.py', req.query.data, req.query.context]);
    // data and context passed as args into the tsHandler.py call, which creates a handler and handles the request
    
    // 'data' is found from passing from tsHandler output as a print statement
    process.stdout.on('data', function(data) {
        res.send(data.toString());
    })
})
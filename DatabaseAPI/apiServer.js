// Basic App Setup
var express = require('express'),
    app = express(),
    port = process.env.PORT || 3001,
    model = require('./models/apiModels');

var routes = require('./routes/apiRoutes');
routes(app);

// Error Handling

// Start the App
app.listen(port);
console.log("DatabaseAPI started successfully on port " + port);
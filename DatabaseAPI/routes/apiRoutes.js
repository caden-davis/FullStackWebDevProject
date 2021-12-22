'use strict';

module.exports = function(app) {
    var controllers = require('../controllers/controllers');

    // Define our API routes
    app.route('/main')
        .get(controllers.getAll)
        .post(controllers.post)
    
    app.route('/main/:ID')
        .get(controllers.getOne)
        .put(controllers.put)
        .delete(controllers.delete)
    app.route('./main/:ID1,:ID2')
        .get(controllers.getRange)
}
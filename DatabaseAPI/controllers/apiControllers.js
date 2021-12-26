'use strict';

// Define database model as variable here
var conn = require('apiModels');

// Define controller functions here
exports.getOne = function(req, res) {
    conn.query(SQLgetOne, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
exports.getAll = function(req, res) {
    conn.query(SQLgetAll, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
exports.getRange = function(req, res) {
    // gets range from req.params.ID1 to req.params.ID2
    conn.query(SQLgetRange, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
exports.delete = function(req, res) {
    // needs req.params.ID
    conn.query(SQLdelete, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
exports.post = function(req, res) {
    // needs both postOne and postAll functionality depending on req
    conn.query(SQLpost, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
exports.put = function(req, res) {
    // aka "update" function
    conn.query(SQLput, (err, queryRes) => {
        if (err) throw err;
        res.json(queryRes);
    })
};
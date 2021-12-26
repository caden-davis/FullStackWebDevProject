// Import Express
var express = require('express'),
app = express(),
port = process.env.PORT || 3001;

'use strict';

// Define database schema
var mysql = require('mysql');
var conn = mysql.createConnection({
    host: "localhost",
    user: "cadendavis",
    password: "Konakona123!"
});

/*
// FIRST TIME SETUP TO CREATE DATABASE
conn.connect((err) => {
    if (err) throw err;
    conn.query("CREATE DATABASE db", function(err, res) {
        if (err) throw err;
    })
})

// FIRST TIME SETUP TO CREATE TABLES
conn.connect((err) => {
    if (err) throw err;
    conn.query("CREATE TABLE t1 (fieldname type, fieldname type)", function(err, res) {
        if (err) throw err;
    })
})
*/

conn.connect((error) => {
    if (error) throw error;
    console.log("Connected to MySQL Database");
});

// Expose the database model (module.exports = db.model)
module.exports = conn;
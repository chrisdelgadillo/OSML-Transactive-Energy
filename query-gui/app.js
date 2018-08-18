var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mongoose = require('mongoose');
mongoose.connect("mongodb://192.168.0.204:27017/query-gui", { useNewUrlParser: true });

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();
var server = require("http").createServer(app);

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/views', express.static('./public/views'));
app.use('/javascripts', express.static('./public/javascripts'));

var port = process.env.port || 3000;

server.listen(port);
console.log("The dirname is "+"-- "+__dirname+" --");
console.log("Listening on port "+port);

module.exports = app;

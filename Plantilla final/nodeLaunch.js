var express = require('express');
require('mongo-connector');
var app = express();
//app.use(express.static(__dirname)); //__dir and not _dir
app.use(express.static(__dirname));
var port = 8000; // you can use any port
app.listen(port);
console.log('server on' + port);
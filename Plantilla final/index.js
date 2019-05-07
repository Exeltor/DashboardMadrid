var express = require('express');


app.use(express.static('public'));



var port = 8080; // you can use any port
app.listen(port);
console.log('server on' + port);
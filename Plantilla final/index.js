var express = require('express');
var app = express();
const MongoClient = require('mongodb').MongoClient;
const url = "mongodb+srv://webReadOnly:readOnly@tpa-whplr.mongodb.net/test?retryWrites=true";
var bodyParser=require("body-parser"); 


app.set('view engine', 'pug');
app.use(bodyParser.urlencoded({
  extended: false
}));

//Directorio de archivos estaticos (CSS, JS no node)
app.use(express.static('public'));

//Dir principal
app.get('/', function(req, res){
  res.render('index', {par:'Init'});
});

//Query de mongo que no se debe perder nunca jamas. Usar esta plantilla para renderizar todas las nuevas paginas que
//requieran mongo.
app.get('/mongo-test', function(req, res){
  MongoClient.connect(url, {useNewUrlParser:true}).then(function (db) {
    dbo = db.db('TPA')
    dbo.collection("tiempoPorHora").findOne({}).then(function(data) {
          res.render('index', {par:JSON.stringify(data)});
    }).catch(function (err) {//failure callback
         console.log(err)
    });
  })
});

var port = 8080;
app.listen(port);
console.log('server on' + port);
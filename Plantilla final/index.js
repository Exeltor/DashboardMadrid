var express = require('express');
var app = express();
const MongoClient = require('mongodb').MongoClient;
const url = "mongodb+srv://webReadOnly:readOnly@tpa-whplr.mongodb.net/test?retryWrites=true";
var request = require('request')
var bodyParser=require("body-parser"); 
var request = require('sync-request');


app.set('view engine', 'pug');
app.use(bodyParser.urlencoded({
  extended: false
}));

//Directorio de archivos estaticos (CSS, JS no node)
app.use(express.static('public'));

//Dir principal
app.get('/', async function(req, res){
  //Aplicable para una coleccion entera
  MongoClient.connect(url, {useNewUrlParser:true}).then(async function (db) {
    dbo = db.db('TPA')

    //Lista general de insercion al index
    var list = {};

    //Llegadas/Salidast
    list.flightDepJsons = await dbo.collection('salidasAeropuerto').find().toArray();
    list.flightArrJsons = await dbo.collection('llegadasAeropuerto').find().toArray();


    //Tiempo
    weatherCallbacks = await dbo.collection('tiempoPorHora').find().sort({'dia/hora': 1}).toArray();

    list.weatherIcon = weatherCallbacks[0].icono;
    list.weatherTemp = weatherCallbacks[0].temp;
    list.weatherDesc = weatherCallbacks[0].desc;
    list.weatherHour = weatherCallbacks[0]['dia/hora'];

    //Metro Lineas
    metroLinesDb = await dbo.collection('lineasMetro').find().sort({'nombre': 1}).toArray();
    list.metroLines = metroLinesDb;

    //Metro Estaciones
    list.metroStations = await dbo.collection('estacionesMetro').find().toArray();

    //Bicimad Estaciones
    list.bicimadStations = await dbo.collection('bicimad').find().toArray();

    //Exchange Rates
    var response = request('GET', 'https://api.exchangeratesapi.io/latest?base=EUR');
    var coinTypeBase= JSON.parse(response.getBody('utf8'));
    list.coinTypes = Object.keys(coinTypeBase.rates);
    list.conversionRatesJson = coinTypeBase.rates;


    //Render final de la pagina con los datos
    res.render('index', list);
    db.close();
  }).catch(function(err){
    console.log(err);
  });
});

//Query de mongo que no se debe perder nunca jamas. Usar esta plantilla para renderizar todas las nuevas paginas que
//requieran mongo.
app.get('/mongo-test', function(req, res){
  MongoClient.connect(url, {useNewUrlParser:true}).then(function (db) {
    dbo = db.db('TPA')
    dbo.collection("tiempoPorHora").findOne({}).then(function(data) {
          //res.render('index', {par:JSON.stringify(data)});
    }).catch(function (err) {//failure callback
         console.log(err)
    });
  })
});

//Navegacion paginas y precarga de paginas
app.get('/servicios/autobus', function(req, res){
  res.render('autobus');
});

app.get('/servicios/bicimad', function(req, res){
  res.render('bicimad');
});

app.get('/servicios/cercanias', function(req, res){
  res.render('cercanias');
});

app.get('/servicios/metro', function(req, res){
  res.render('metro');
});

app.get('/servicios/uber', function(req, res){
  res.render('uber');
});

app.get('/servicios/vuelos', function(req, res){
  res.render('vuelos');
});

app.get('/eventos', function(req, res){
  res.render('eventos');
});

app.listen(process.env.PORT || 8080);
console.log('server on');
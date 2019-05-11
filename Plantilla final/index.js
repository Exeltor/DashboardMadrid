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
    list.distinctLines = await dbo.collection('estacionesMetro').distinct('linea');

    //Cercanias
    list.cercaniasStations = await dbo.collection('paradasCercanias').find().toArray();

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

//Navegacion paginas y precarga de paginas
app.get('/servicios/autobus', function(req, res){
  MongoClient.connect(url, {useNewUrlParser:true}).then(async function (db) {
    dbo = db.db('TPA')

    //Lista general de insercion al index
    var list = {};

    list.busStations = await dbo.collection('paradasEMT').find().toArray();

    res.render('autobus', list);
    db.close();
  }).catch(function(err){
    console.log(err);
  });
});

app.get('/servicios/bicimad', function(req, res){
  MongoClient.connect(url, {useNewUrlParser:true}).then(async function (db) {
    dbo = db.db('TPA')

    //Lista general de insercion al index
    var list = {};

    list.bicimadStations = await dbo.collection('bicimad').find().toArray();

    function contains(arr, key, val){
      for(var i = 0; i < arr.length; i++){
        if(arr[i][key] === val) return true;
      }

      return false;
    }


    if(contains(list.bicimadStations, "operativo", "No")){
      list.bicimadStationsOff = true;
    } else {
      list.bicimadStationsOff = false;
    }

    //Render final de la pagina con los datos
    res.render('bicimad', list);
    db.close();
  }).catch(function(err){
    console.log(err);
  });
});

app.get('/servicios/metro-cercanias', function(req, res){
  MongoClient.connect(url, {useNewUrlParser:true}).then(async function (db) {
    dbo = db.db('TPA')

    //Lista general de insercion al index
    var list = {};

    //Metro Lineas
    metroLinesDb = await dbo.collection('lineasMetro').find().sort({'nombre': 1}).toArray();
    list.metroLines = metroLinesDb;

    //Metro Estaciones
    list.metroStations = await dbo.collection('estacionesMetro').find().toArray();
    list.distinctLines = await dbo.collection('estacionesMetro').distinct('linea');

    //Cercanias
    list.cercaniasStations = await dbo.collection('paradasCercanias').find().toArray();

    //Render final de la pagina con los datos
    res.render('metro-cercanias', list);
    db.close();
  }).catch(function(err){
    console.log(err);
  });
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
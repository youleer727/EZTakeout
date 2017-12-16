var gzippo = require('gzippo');
var express = require('express');
var geoip = require('geoip-lite');
const yelp = require('yelp-fusion');
var bodyParser = require('body-parser');
var config = require('./config');
var PythonShell = require('python-shell');

const client_id = config.client_id;
const client_secret = config.client_secret;

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.post('/ip', function(req, res) {
    var ip = req.headers['x-forwarded-for'] ||
            req.connection.remoteAddress ||
            req.socket.remoteAddress ||
            req.connection.socket.remoteAddress;
    var geo = geoip.lookup(ip);
    if (geo == null) {
        res.send({
            lat: null,
            long: null,
            error: true
        })
    }
    var lat = geo.ll[0];
    var long = geo.ll[1];
    response = {
        lat: lat,
        long: long,
        error: false
    };
    res.send(response);
});

app.post('/yelp', function(req, res) {
    console.log('receiving request from frontend');
    console.log(req.body);
    var month = req.body.day + 1;
    var day = req.body.day;
    var hour = Number(req.body.hour);
    var time_range = Number(req.body.time_range);
    var foodtype = req.body.food_type;
    var cost_range = Number(req.body.cost_range);
    var lat = req.body.lat;
    var long = req.body.long;
    var limit = req.body.limit;
    function convertMileToMeters(i) {
        return Math.floor(i*1609.344);
    }
    var passenger_count = '1';
    //TODO: handle the format of hour
    var options = {
        args:[hour.toString(), passenger_count, cost_range.toString(), time_range.toString()]
    };
    var radius = null;
    var getRadius = function() {
        return new Promise(function(resolve, reject) {
            PythonShell.run('model_predict.py', options, function (err, results) {
                if (err) reject(err);
                else {
                    radius = convertMileToMeters(Number(results[0]));
                    resolve(radius);
                    // radius = 500;
                    console.log('radius is ' + radius);
                }
            })
        })
    };

    getRadius().then(function() {
        const searchRequest = {
            term: req.body.food_type,
            latitude: lat,
            longitude: long,
            radius: radius,
            limit: req.body.limit
        };
        yelp.accessToken(client_id, client_secret).then(response => {
            const client = yelp.client(response.jsonBody.access_token);
        client.search(searchRequest).then(response => {
            console.log("Found " + response.jsonBody.businesses.length + " restaurants");
        if (response.jsonBody.businesses.length < 1) {
            console.log("Zero results");
        }
        res.send(response.jsonBody.businesses);
    });
    }).catch(e => {
            console.log(e);
    });
    });
});

app.use(express.logger('dev'));
app.use(gzippo.staticGzip("" + __dirname + "/app"));
var port = process.env.PORT || 5000;
app.listen(port);
console.log("Listening on " + port + "!");
console.log("Go to http://localhost:" + port);
var express = require('express');
var router = express.Router();
var grpc = require('grpc');
var rpc = require('node-json-rpc');
var PROTO_PATH = __dirname + '/../../grpc/examples/protos/helloworld.proto';

/* GET home page. */
router.get('/', function (req, res, next) {
});
/*
router.get('/grpc', function (req, res, next) { 
  var hello_proto = grpc.load(PROTO_PATH).helloworld;
  function main() {
    var client = new hello_proto.Greeter('localhost:50051', grpc.credentials.createInsecure());
    var data;
    if (process.argv.length >= 3) {
      data = process.argv[2];
    } else {
      data = 'erick';
    }
    //{ method: function(){} }
    client.sayHello({ name: data }, function (err, response) {
      console.log(response);
      console.log('Greeting:', response.message);
    });
  }
  main();
});
*/
router.get('/jsonrpc', function (req, res, next) {
  var options = {
    // int port of rpc server, default 5080 for http or 5433 for https
    port: 22916,
    // string domain name or ip of rpc server, default '127.0.0.1'
    host: '192.168.0.105',
    // string with default path, default '/'
    path: '/',
    // boolean false to turn rpc checks off, default true
    strict: true
  };

  // Create a server object with options
  var client = new rpc.Client(options);
  client.call(
    {
      "jsonrpc": "2.0",
      "method": "list_platforms", //platforms.uuid.fedf5395-c908-4690-8410-13fee500a0d0.start_agent
      "authorization": "LnpKXuJK4IskkjQLqxJSoGmd0xHCGXQMxx15wnLhpx0",
      "id": 0
    },
    function (err, res) {
      // Did it all work ?
      if (err) { console.log(err); }
      else { console.log(res); }
    }
  );
});
module.exports = router;

var express = require('express');
var router = express.Router();
var path = require('path');
var Energy = require(path.join(__dirname,"../","/public/models/energy.js"));






/* GET home page. */
router.get('/', function(req, res, next) {
  //res.render('index', { title: 'Express' }); *this was the default 
  res.status(200).sendFile(path.join(__dirname,"../","/public/views/index.html"));
});
router.post('/queryPost', function(req, res, next){
  var energy = new Energy(req.body);
  energy.save(next);
  res.status(200).json(req.body);
});
router.get('/queryAll', function(req, res, next){
  Energy.find({}, function(err,infolist){
    console.log(infolist)
    if(err){return next(err)};
    res.status(200).json(infolist);
  });
});

module.exports = router;

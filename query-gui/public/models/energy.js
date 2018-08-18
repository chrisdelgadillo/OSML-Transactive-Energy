var mongoose = require('mongoose');

var energySchema = mongoose.Schema({
    energyReading: { type: Number , required: true},
    buyerId: { type: String , required: true },
    sellerId: { type: String , required: true},
    timeStamp: { type: String , required: true , unique: true}
});

var Energy = mongoose.model("Energy", energySchema);
module.exports = Energy;
/*
//This 
async function transaction(Transaction){ //this is our Transaction 
    const contract = Transaction.electricity.contract; //this is the contract we defined within our asset
    const electricity = Transaction.electricity; //this is our asset
    
}
*/
async function transaction (Transaction) //Transaction is our transaction created in the .cto file 
 {
 	const contract = Transaction.electricity.contract; //this is the contract we defined within our asset
 	const electricity = Transaction.electricity;//variable that represents electricity function with all of it's parameters
 	let payout = contract.unitPrice * electricity.unitCount; //variable represents transaction payout
    
 	console.log('Received at: ' + contract.timestamp); //print out timestamp (the time at which the transaction was made)

    //Set status of shipment
	electricity.status = 'COMPLETED';
	
	/*
	if(seller.batteryWattage >= electricity.unitCount)
	if(buyer.accountBalance >= payout)
	*/

   
 }


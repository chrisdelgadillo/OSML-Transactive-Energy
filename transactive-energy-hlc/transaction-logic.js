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
 	let transactionOutput = contract.unitPrice * electricity.unitCount; //variable represents transaction output
    
 	console.log('Received at: ' + contract.timestamp); //print out timestamp
    console.log('Contract arrivalDateTime: ' + contract.arrivalDateTime); //print out arrival Date

    //Set status of shipment
    electricity.status = 'Arrived';

    //if shipment did not arrive, set payment to 0
    if(Transaction.timestamp > contract.arrivalDateTime) 
    	 {
    	 	transcriptOutput = 0;
    	 	console.log('Late shipment');
    	 }
   
 }


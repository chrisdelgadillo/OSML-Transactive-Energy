#JSON Blockchain request and reponse 
import time
import os.path
import json
#import RPi.GPIO as IO

relayPin = 4

def parse_request(attribute):
	with open('query_1.json') as f:
		query_data = json.load(f)
	return query_data[attribute]

# def transfer_power(query_x):
# 	current = read_from_scrape(current_sys_transfer)
# 	vinit   = read_from_scrape(volt_sys_1)
# 	vcharge = query_x.energy_request/current
# 	vfinal  = vinit + vcharge
# 		while vinit <= vfinal:
# 			activate_relay()
# 			print('Energy Transfer in progress...')
# 			time.sleep(1)

# def check_transaction(transaction):
# 	if transaction == true:
# 		if check_asset() == true:
# 			transfer_power()
# 	else:
# 		print('Unable to transfer power.')
# 		return	

def check_asset(queryreq):
	if queryreq.seller_energy < queryreq.energy_request or queryreq.seller_energy <= 0:
		print('Insufficient asset requirements.')
		return False
	else:
		print('Asset requirements met.')
		return True

# def pinSetup(Pin):
# 	IO.setmode(IO.BCM)
# 	IO.setwarnings(False)
# 	IO.setup(Pin,IO.OUT)

# def activate_relay():

def check_query_exists(filename):
	file = filename + '.json'
	if os.path.exists(file) == True:
		return True
	else:
		return False

def assign_object(object_name):
	object_name = query(parse_request('queryID'),
				  parse_request('energy_request'),
				  parse_request('buyer_energy'),
				  parse_request('seller_energy'),
				  parse_request('buyerID'),
				  parse_request('sellerID'), 
				  parse_request('time'))
	print(query)

class current_data():

	def __init__(self,seller_energy,buyer_energy,sellerID, buyerID,time):

	def create_json(self):
		with open('query.json','w') as outfile:
			json.dump(self.__dict__,outfile)
		print('JSON created.')


class query():
	
	def __init__(self,queryID,energy_request,buyer_energy,seller_energy,buyerID,sellerID,time):
		self.queryID        = queryID
		self.energy_request = energy_request
		self.buyer_energy   = buyer_energy
		self.seller_energy  = seller_energy
		self.buyerID        = buyerID
		self.sellerID       = sellerID
		self.time	        = time

	def create_json(self):
		with open('query.json','w') as outfile:
			json.dump(self.__dict__,outfile)
		print('JSON created.')


'''

Define variables parsed from BC query request (JSON file).

'''

queryID_par        = parse_request('queryID')
energy_request_par = parse_request('energy_request')
buyer_energy_par   = parse_request('buyer_energy')
seller_energy_par  = parse_request('seller_energy')
buyerID_par        = parse_request('buyerID')
sellerID_par       = parse_request('sellerID')
time_par           = parse_request('time')

t = True
while t:
	for i in range(1,10):
		query_file = 'query_'+ str(i)
		if check_query_exists(query_file) == True:
			print('New blockchain query has been identified.')
			time.sleep(2)
			print(str(queryID_par) + ':' + str(buyerID_par) + ' is requesting ' + str(energy_request_par) + ' watts from ' + str(sellerID_par))
			var = raw_input('Proceed? (y/n):')
			if var == 'y':

				print('Performing Transaction...')
			else:
				print('Transaction denied.')
			break
		else:
			pass

	time.sleep(10)
# check_asset(query_1)
#print(query.seller_energy(query_1))
#check_asset(query_1.seller_energy(),query_1.energy_request())
#query.create_json(query_1)
# parse_request()def transfer_power(query_x):
# 	current = read_from_scrape(current_sys_transfer)
# 	vinit   = read_from_scrape(volt_sys_1)
# 	vcharge = query_x.energy_request/current
# 	vfinal  = vinit + vcharge
# 		while vinit <= vfinal:
# 			activate_relay()
# 			print('Energy Transfer in progress...')
# 			time.sleep(1)
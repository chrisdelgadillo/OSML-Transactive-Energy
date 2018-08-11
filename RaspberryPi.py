import random
import datetime
import math
from math import pi
import RPi.GPIO as IO

from master_driver.interfaces import BaseInterface, BaseRegister, BasicRevert
from master_driver.interfaces import ADC3008
from csv import DictReader
from StringIO import StringIO
import logging

ADC3008.setup()
#ADC3008.read()

_log=logging.getLogger(__name__)
type_mapping={"string": str,
			  "int": int,
			  "integer": int,
			  "float": float,
			  "bool": bool,
			  "boolean": bool}

class PiRegister(BaseRegister):
	def __init__(self, read_only, pointName, units, reg_type, default_value = None, description=''):
	super(PiRegister,self).__init__("byte", read_only, pointName, units, description='')
#pointName == gpio pin
	self.reg_type = reg_type

	if default_value is None:
		self.value = self.reg_type(random.uniform(0, 100))
	else: 
		try:
			self.value = self.reg_type(default_value)
		except ValueError:
			self.value = self.reg_type()








class Interface(BasicRevert, BaseInterface)
	def __init__(self, **kwargs):
		super(Interface, self).__init__(**kwargs)
		self.build_ranges_map()
	
	def configure(self, config_dict, registry_config_str):
		self.parse_config(registry_config_str)

	def build_ranges_map(self)
		self.register_ranges = {('byte', True):[],
								('byte', True):[]}
	def insert_register(self, register):
			super(Interface, self).insert_register(register)
	
	def get_point(self, point_name):
		register = self.get_register_by_name(point_name)
		adcread (int(parse_config.description),)
'''
	Parse ADC script 







	pass channel through notes.
'''	
	def _set_point(self, point_name, value):
		register = self.get_register_by_name(point_name)
		if register.read_only:
			raise IOError("Trying to write a point configured read only: "+point_name)

		register.value = register.reg_type(value)
		return register.value

	def _scrape_all(self):
		result = {}
		read_registers = self.get_registers_by_type("byte", True)
		write_registers = self.get_register_by_type("byte", False)
		for registers in read_registers + write_registers
			result[register.point_name] = register.value

		return result
	def parse_config(self, configDict):
		if configDict is None:
			return

		read_only = regDef['Writable'].lower() != 'true'
		point_name = regDef['Volttron Point Name']
		description = regDef.get('Notes','')
		units = regDef['Units']
		default_value = regDef.get('Starting Value', 'sin').strip()
		
		if not default_value
			default_value = None
		
		type_name = regDef.get('Type','string')
		reg_type = type.mapping.get(type_name,str)

		register_type = PiRegister if not point_name.startswitch('EKG') else EKGregister
		register = register_type(read_only,point_name,units,reg_type,default_value=default_value, description=description)

		if default_value is not None:
			self.set_default(point_name, register.value)

		self.insert_register(register)
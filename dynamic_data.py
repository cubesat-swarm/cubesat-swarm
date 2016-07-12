"""
Author: Aryadne Rezende
Date: Jul 9, 2016
Project: Swarm
Contatc: aryadneccomp@gmail.cosmos
Function: This class provides the functions for DynamicData access
"""


import sqlite3
from time import time

class DynamicData:

	conn = sqlite3.connect('smember.db', check_same_thread=False)
	c = conn.cursor()
	
	def __init__(self, i, d, u, v, t):
		self.id = i
		self.value = v
		self.description = d
		self.unit = u
		self.timestamp = t


	def get_data_db(self,id):
		self.c.execute("SELECT * FROM dynamic_data WHERE id = " + str(id))
		d = self.c.fetchone()
		if(d!=None):
			return DynamicData(d[0],d[1],d[2],d[3],d[4])
		else:
			return None 

	def get_info(self,id):
		item = self.get_data_db(id)
		if(item!=None):
			return str(item.id) +","+ str(item.value)+","+str(item.unit)+","+str(item.timestamp)
		else:
			return "not found"

	def update_values(self):
		params=(self.value,self.timestamp,self.id)
		self.c.execute("UPDATE dynamic_data SET value=?, timestamp=? WHERE id=?",params)
		self.conn.commit()


	def fill_table(self):
		DynamicData(3,"voltage_main_cpu","volts",0.0,time()).save_data_db()


	def save_data_db(self):
		params = (self.id, self.description,self.unit, self.value,self.timestamp)
		self.c.execute("INSERT INTO dynamic_data VALUES (?,?,?,?,?)",params)
		self.conn.commit()


#d = DynamicData(1,"","",0.0,time())
#d.update_values()
#d = d.get_data_db(4)
#print("Dynamic data: "+str(d.id)+","+str(d.value)+","+d.description+","+str(d.unit)+","+str(d.timestamp))
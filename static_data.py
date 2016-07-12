"""
Author: Aryadne Rezende
Date: Jul 9, 2016
Project: Swarm
Contatc: aryadneccomp@gmail.com
Function: This class provides the functions for StaticData access
"""


import sqlite3

class StaticData:

	conn = sqlite3.connect('smember.db', check_same_thread=False)
	c = conn.cursor()

	def __init__(self, i, v, d, u):
		self.id = i
		self.value = v
		self.description = d
		self.unit = u

	def get_data_db(self,id):
		#self.c.execute("SELECT * FROM static_data WHERE id ='"+repr(id)+"'")
		self.c.execute("SELECT * FROM static_data WHERE id = " + id)

		#print(self.c.fetchone())
		d = self.c.fetchone()
		if(d!=None):
			return StaticData(d[0],d[1],d[2],d[3])
		else:
			return None

	def get_info(self,id):
		item = self.get_data_db(id)
		if(item!=None):
			return str(item.id) +","+ str(item.value)+","+str(item.unit)
		else:
			return "not found"

	def save_data_db(self):
		params = (self.id, self.value, self.description,self.unit)
		self.c.execute("INSERT INTO static_data VALUES (?,?,?,?)",params)
		self.conn.commit()


	def fill_table():
		StaticData(1,"4","cpu_cores","Main_CPU").save_data_db()
		StaticData(2,"A7","arch","").save_data_db()
		#... put the next attributes

#data = StaticData(1,"4","cpu_cores","Main_CPU")
#data.save_data_db()
#print(data.has_sensor(1))

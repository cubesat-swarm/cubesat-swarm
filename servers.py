"""
Author: Aryadne Rezende
Date: Jul 9, 2016
Project: Swarm
Contatc: aryadneccomp@gmail.com
Function: This will be a server to recieve and handle messages from pi and from cosmos
"""

import socket
from threading import *
import struct
from static_data import StaticData
from dynamic_data import DynamicData

class GeneralServer(Thread):
	def __init__(self, add, source):
		Thread.__init__(self)
		self.source = source
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ip = add.split(',')[0]
		port = add.split(',')[1]
		server_adress = (ip,int(port))
		self.serversocket.bind(server_adress)
		print("Serving to "+add)
		self.start()

	def run(self):
		while True:
			data, addr = self.serversocket.recvfrom(32)
			print("Received: %s"%str(data))
			print("From: "+str(addr))
			if(self.source == "pi"):
				#returns the response
				resp = self.pi_request_process(data)
			if(self.source == "cosmos"):
				resp = self.cosmos_request_process(data)
			r = bytes(str(resp),'utf-8')
			self.serversocket.sendto(r,addr)

	def pi_request_process(self,resp):
		request = resp.decode('utf-8')
		type_d = request.split(',')[0]
		id_d = request.split(',')[1]
		if(type_d=="1"):
			d = StaticData("","","","")
			answer = d.get_info(id_d)
		else:
			d = DynamicData(0,"","",0,0)
			answer = d.get_info(id_d)
		return answer

	def cosmos_request_process(self,resp):
		dataUnpacked = struct.unpack('>BBH',command) #unpacks two unsigned chars and one short
		print('Command Length: ',dataUnpacked[0])
		print('Command ID: ',dataUnpacked[1])
		print('Command Sensor_ID: ', dataUnpacked[2])
		#makes a query asking for the sensor_id
		d = StaticData("","","","")
		resp = d.has_sensor(dataUnpacked[2])
		package = make_tlm(resp)
		return package

	#makes the telemetry packages
	def make_tlm(resp):
		return ""

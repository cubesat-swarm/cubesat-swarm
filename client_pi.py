"""
Author: Aryadne Rezende
Date: Jul 9, 2016
Project: Swarm
Contatc: aryadneccomp@gmail.com
Function: This code will provide client functions to send menssages to the swarm members
"""

import socket
import sqlite3


def get_address_pi(pi):
	conn = sqlite3.connect('smember.db', check_same_thread=False)
	c = conn.cursor()
	c.execute("SELECT * FROM swarm WHERE id = " + str(pi))
	d = c.fetchone()
	conn.close()
	if(d!=None):
		return d[1]
	else:
		return None

#sends a query(sensor id) to another pi
def make_query(query,address):
	ip = address.split(',')[0]
	port = address.split(',')[1]
	print("Sending "+ query.decode('utf-8')+ " to pi ip "+ ip)
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serversocket.sendto(query,(ip,int(port)))
	data, server = serversocket.recvfrom(32)
	return data

def ask_pi(query,pi):
	#query = b'2,1'
	add = get_address_pi(pi)
	return make_query(query,add).decode('utf-8')

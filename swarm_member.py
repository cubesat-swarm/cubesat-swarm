"""
Author: Aryadne Rezende
Date: Jul 11, 2016
Project: Swarm
Contatc: aryadneccomp@gmail.com
Function: This is a member of swarm
"""

from servers import GeneralServer
from client_pi import get_address_pi,ask_pi

class SwarmMember:

	def __init__(self,id_p):
		self.id = id_p
		self.start_servers()

	def start_servers(self):
		add = get_address_pi(self.id)
		#GeneralServer('127.0.0.1,8081',"pi")
		GeneralServer(add,"pi")
		#GeneralServer(add2,"cosmos") < another door!
		return 0

	def ask(self,query,pi):
		ans = ask_pi(query,pi)
		print(ans)
		return ans

s = SwarmMember(1)
s.ask(b'1,1',2)

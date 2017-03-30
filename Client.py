# python 3.6 client

import socket

Sockets=[]

class MakeSocket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock=sock
			
	def connect(self, host, port):
		self.sock.connect((host, port))
		
	def send

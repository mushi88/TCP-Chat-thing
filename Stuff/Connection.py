import socket
import threading

class Connect():
	def __init__(self, Port=2345, IP="localhost"):
		sock=socket.socket(AF_INET, SOCK_STREAM)
		self.sock=sock
		try:
			self.sock.connect((IP,PORT))
			self.is_connected=True
			return "Connected."
		except:
			self.is_connected=False
			return "Failed to connect."
			
	def Send(self,Value):
		if type(Value)!=str:
			Value=str(Value)
			
		self.sock.send(bytes(Value, "utf-8"))
	
	def Recive(self)

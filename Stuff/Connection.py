import socket

class Connect():
	def __init__(self, Port=2345, IP="localhost", Buffer=10240):
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
	
	def Recive(self):
		try:
			Data=str(self.sock.recv(10240), "utf-8")
			return Data
		except:
			return "Failed to recieve data."
	

import socket
import threading

class Connect:
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
	
class PortScan:
        def __init__(self, HostIP="localhost"):
                self.HostIP=HostIP

        def Go(self):
                threads=[]
                output={}
                ports=[]

                for x in range(4000,5000):
                        t=threading.Thread(target=self.Connect, args=(self.HostIP, x, output))
                        threads.append(t)

                for x in range(4000,5000):
                        threads[x].start()

                for x in range(4000,5000):
                        threads[x].join()
                        
                for x in range(4000,5000):
                        if not output[x]==None:
                                ports.append(output[x])
                
                return ports

        def Connect(self, IP, x, output):
                PortScan=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                PortScan.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                PortScan.settimeout(1)
                try:
                    PortScan.connect((IP, x))
                    output[x]=str(x)
                except:
                    output[x]=None
        
	

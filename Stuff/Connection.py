import socket
import threading

class Connect:
        def __init__(self, Port=2345, IP="localhost", Buffer=10240):
                sock=socket.socket(AF_INET, SOCK_STREAM)
                self.sock=sock
                try:
                        self.sock.connect((IP,PORT))
                        self.is_connected=True
                except:
                        self.is_connected=False
                        
        def Send(self,Value):
                if type(Value)!=str:
                        Value=str(Value)
                        
                self.sock.send(bytes(Value, "utf-8"))

        def Recive(self):
                try:
                        Data=str(self.sock.recv(10240), "utf-8")
                        return Data
                except:
                        return False
	
class PortScan:
        def __init__(self, HostIP="localhost"):
                self.HostIP=HostIP

        def Go(self):
                threads=[]
                output={}
                ports=[]

                print("Scanning ports 2000-3000 on {}...".format(self.HostIP))

                for x in range(2000, 3000):
                        t=threading.Thread(target=self.Connect, args=(self.HostIP, x, output))
                        threads.append(t)

                for y in range(0, len(threads), int(len(threads)/100)):
                        for x in range(y,int(y+len(threads)/100)):
                                threads[x].start()

                        for x in range(y,int(y+len(threads)/100)):
                                threads[x].join()
                        
                        
                for x in range(2000, 3000):
                        if not output[x]==None:
                                ports.append(output[x])

                
                return ports

        def Connect(self, IP, x, output):
                PortScan=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                PortScan.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                PortScan.settimeout(.1)
                try:
                    PortScan.connect((IP, x))
                    output[x]=str(x)
                except:
                    output[x]=None
        
	

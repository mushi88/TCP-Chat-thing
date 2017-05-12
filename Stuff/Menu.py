from tkinter import *
import Connection
import threading
import time

class Window(Frame):
        def __init__(self, master=None, UCL=None):
                Frame.__init__(self, master)
                self.master=master
                self.UCL=UCL
                self.Load_UI()
                #thread=threading.Thread(target=self.Start)
                #thread.start()
    
        def Load_UI(self):
                self.MenuBar=Menu(self)
                self.ConnectMenu=Menu(self.MenuBar,tearoff=0)
                self.ConnectMenu.add_command(label="Lan", command=self.Lan_UI)

                self.MenuBar.add_cascade(label="Connect", menu=self.ConnectMenu)

                self.master.title("Kirsi's Python Chat")
                self.master.config(menu=self.MenuBar)
                width,height=self.master.winfo_screenwidth(), self.master.winfo_screenheight()
                self.master.geometry("%dx%d+0+0" % (width, height))
                self.pack(fill=BOTH, expand=1)

                self.LanUI=Label(self) # LANGUI
                self.LanUI.pack(fill=BOTH, expand=1)

                self.Lan_Servers=Frame(self.LanUI)
                self.Lan_Servers.pack(fill=BOTH, expand=1)
                #self.Lan_Servers.config(state=DISABLED)

                self.Lan_Status=Text(self.LanUI)
                self.Lan_Status.pack(fill=BOTH, expand=1)
                self.Lan_Status.insert("end", "------------- Status:\n\n")
                self.Lan_Status.config(state=DISABLED)

                self.LanUI.pack_forget()
                
                self.ChatUI=Label(self) # CHATGUI
                self.ChatUI.pack(fill=BOTH, expand=1)
                
                self.ChatFrame=Frame(self.ChatUI, height=10)
                self.ChatFrame.pack(fill=BOTH, expand=1)
                
                self.ChatLog=Text(self.ChatUI)
                self.ChatLog.pack(fill=BOTH, expand=1)
                self.ChatLog.config(state=DISABLED)
                
                self.ChatUI.pack_forget()

        def Lan_UI(self):
                self.LanUI.pack(fill=BOTH, expand=1)
                self.UpdateStatus(self.Lan_Status, "Searching for servers on LAN...")

                time.sleep(1)
        
                PortScanner=Connection.PortScan()
                Ports=PortScanner.Go()
                
                self.Frames=[]
                
                for x in range(len(Ports)):
                    #self.UpdateStatus(self.Lan_Servers, "Found server on port {}.".format(Ports[x]))
                    frame=Frame(self.Lan_Servers)
                    frame.pack()
                    
                    button=Button(frame, text="Join", command=lambda: self.JoinServer(Ports[x], "localhost"))
                    button.pack(left)
                    
                    label=Label(frame, text="Port: {}               Host: {}".format(Port[x], "localhost"))
                    label.pack()
                    
                    self.Frames.append(frame)
                    
                self.UpdateStatus(self.Lan_Status, "Found {} servers.".format(len(Ports)))

        def UpdateStatus(self, Txt, New):
                Txt.config(state=NORMAL)
                Txt.insert("end", New+"\n")
                Txt.config(state=DISABLED)
        
        def JoinServer(self, port, host):
            conn=Connection.Connect(Port=port, IP=host)
            if conn.is_connected:
                self.ChatGui()
            else:
                self.UpdateStatus(self.Lan_Status, "Failed to connect to {}:{}".format(port, IP))
            self.conn=conn
        
        def ChatGui(self):
            self.ChangeGuiType()
            self.ChatUI.pack(fill=BOTH, expand=1)
            
            self.UCL()
        
        def ChangeGuiType(self):
            self.LanUI.pack_forget()

class UpdateChatLog(threading.Thread):
    def __init__(self):
        super(UpdateChatLog, self).__init__()
        self._stop_event = threading.Event()
    
    def stop(self):
        self._stop_event.set()
        
    def stopped(self):
        return self._stop_event.is_set()

root=Tk()
#root.resizable(False, False)
App=Window(root, UpdateChatLog)
root.mainloop()

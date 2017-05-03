from tkinter import *
import Connection
import threading

class Window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.root=root
                self.master=master
                self.Load_UI()
                self.Mode=None
                thread=threading.Thread(target=self.Start)
                thread.start()
	
        def Load_UI(self):
                self.MenuBar=Menu(self)
                self.ConnectMenu=Menu(self.MenuBar,tearoff=0)
                self.ConnectMenu.add_command(label="Connect", command=self.Lan_UI)

                self.MenuBar.add_cascade(label="Connect", menu=self.ConnectMenu)

                self.master.title("Kirsi's Python Chat")
                self.master.config(menu=self.MenuBar)
                self.pack(fill=BOTH, expand=1)

                self.LanUI=Label(self)
                self.LanUI.pack(fill=BOTH, expand=1)

                self.Lan_Servers=Text(self.LanUI)
                self.Lan_Servers.pack(fill=BOTH, expand=1)
                self.Lan_Servers.config(state=DISABLED)

                self.Lan_Status=Text(self.LanUI)
                self.Lan_Status.pack(fill=BOTH, expand=1)
                self.Lan_Status.insert("end", "------------- Status:\n\n")
                self.Lan_Status.config(state=DISABLED)

                self.LanUI.pack_forget()

        def Lan_UI(self):
                self.LanUI.pack(fill=BOTH, expand=1)
                self.UpdateStatus(self.Lan_Status, "Searching for servers on LAN...")

        def UpdateStatus(self, Txt, New):
                Txt.config(state=NORMAL)
                Txt.insert("end", New+"\n")
                Txt.config(state=DISABLED)
                

        def Start(self):
                print("LOL")

root=Tk()
#root.resizable(False, False)
App=Window(root)
root.mainloop()

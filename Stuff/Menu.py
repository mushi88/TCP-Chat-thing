from tkinter import *

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
        self.master=master
        self.Load_UI()
        thread=threading.Thread(target=self.Start)
        thread.start()
	
	def Load_UI(self):
		self.master.title("Kirsi's Python Chat")
		
		
		self.MenuBar=Menu(self)
		self.ConnectMenu=Menu(self.MenuBar,tearoff=0)
		self.ConnectMenu.add_command(label="Connect", command=self.Lan_UI)
		
		self.MenuBar.add_cascade(label="Connect", menu=self.ConnectMenu)
		
		self.config(menu=self.MenuBar)
		
		self.pack(fill=BOTH, expand=1)

	def Lan_UI(self):
		print("LOL")

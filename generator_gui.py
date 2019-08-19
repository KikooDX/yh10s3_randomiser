"""A You Have 10 Seconds 3 unofficial expansion made by KikooDX
kikoodata.000webhostapp.com"""

from modules.loadRooms import *
from modules.createFrame import *
from modules.drawRoom import *
from generator import *
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.height = 200
        self.width = 120

    def init_window(self):      
        self.master.title("YH10S3 randomiser")
        self.pack(fill=BOTH, expand=1)
        button = Button(self, text="Generate", command=main)
        button.place(relx=0.5, rely=0.5, anchor=CENTER)

root = Tk()
root.geometry("200x120")
app = Window(root)
root.mainloop()

from tkinter import*
from tkinter import messagebox
from Ventanas import Login


class Manager(Tk):
    
    def __init__(self,*args,**Kwargs):
        super().__init__(*args,**Kwargs)
        self.title("SISTEMA")
        self.geometry("1200x900")
        container = Frame(self)
        container.pack(side=TOP,fill=BOTH,expand=True)
        container.configure(bg="green")
        Login(container,self).tkraise()

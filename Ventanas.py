from tkinter import *
from tkinter import ttk,messagebox

class Login(Frame):

    def __init__(self,padre,controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=1200,height=900)
        self.controlador = controlador
        self.widgets()

    def widgets(self):
        fondo = Frame(self,bg="black")
        fondo.pack()
        fondo.place(x=0,y=0,width=1200,height=900)
        self.username = Entry(fondo)
        self.username.place(x=580,y=440)
        self.password = Entry(fondo,show="*")
        self.password.place(x=580,y=480)
        btn1 = Button(fondo,bg="blue",fg="white",text="Iniciar")
        btn1.place(x=580,y=520)
        btn2 = Button(fondo,bg="blue",fg="white",text="Registrar")
        btn2.place(x=640,y=520)
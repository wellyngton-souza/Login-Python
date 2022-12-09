import customtkinter
from tkinter import *

def Logou():
    window = customtkinter.CTk()
    window.geometry("640x360")
    window.title("App")
    window.resizable(False, False)

    label = customtkinter.CTkLabel(window, text="Você está Logado")
    label.place(x=300, y=150)

    window.mainloop()
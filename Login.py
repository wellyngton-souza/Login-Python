import customtkinter
from tkinter import *

import cadastro.Cadastro as Cadastro

import LG_config

window = customtkinter.CTk()
window.geometry("640x360")
window.title("App")
window.resizable(False, False)

label = customtkinter.CTkLabel(window, text="Login")
label.place(x=291, y=92)

textbox1 = customtkinter.CTkEntry(window, width=137, height=25, placeholder_text="Gmail")
textbox1.place(x=252, y=126)
textbox2 = customtkinter.CTkEntry(window, width=137, height=25, placeholder_text="Senha")
textbox2.place(x=252, y=165)

button1 = customtkinter.CTkButton(window, width=137, height=25, text="Logar", command=LG_config.create_server_connection)
button1.place(x=252, y=204)
button2 = customtkinter.CTkButton(window, width=137, height=25, text="Cadastrar", command=Cadastro.Cadastrar)
button2.place(x=251,y=243)

window.mainloop()
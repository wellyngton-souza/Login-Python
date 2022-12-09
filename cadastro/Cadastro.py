from tkinter import *
import customtkinter
import cadastro.CD_config as CD_config

def Cadastrar():

    window = customtkinter.CTk()
    window.geometry("640x360")
    window.title("App")
    window.resizable(False, False)

    label = customtkinter.CTkLabel(window, text="Cadastrar")
    label.place(x=288, y=92)

    textbox1 = customtkinter.CTkEntry(window, width=137, height=25, placeholder_text="Nome")
    textbox1.place(x=252, y=126)
    textbox2 = customtkinter.CTkEntry(window, width=137, height=25, placeholder_text="Gmail")
    textbox2.place(x=252, y=165)
    textbox3 = customtkinter.CTkEntry(window, width=137, height=25, placeholder_text="Senha")
    textbox3.place(x=252, y=204)

    button2 = customtkinter.CTkButton(window, width=137, height=25, text="Cadastrar", command=CD_config.create_server_connection)
    button2.place(x=251,y=243)

    window.mainloop()
import request2
import customtkinter

#interface
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela_cadastro = customtkinter.CTk()
janela_cadastro.geometry("500x300")

def clique():
    print("Fazer login")

texto = customtkinter.CTkLabel(janela_cadastro, text ="Fazer Login")
texto.pack(padx = 10, pady = 10)

email_login = customtkinter.CTkEntry(janela_cadastro, placeholder_text = "Digite seu email")
email_login.pack(padx = 10, pady = 10)

senha_login = customtkinter.CTkEntry(janela_cadastro, placeholder_text = "Digite sua senha", show = "*")
senha_login.pack(padx = 10, pady = 10)

checkbox = customtkinter.CTkCheckBox(janela_cadastro, text= "Lembrar login")
checkbox.pack(padx =10, pady = 10)

botao = customtkinter.CTkButton(janela_cadastro, text = "login", command=clique)
botao.pack(padx = 10, pady = 10)


janela_cadastro.mainloop()

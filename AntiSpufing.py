# importar as bibliotecas --------------------------------------------------
import customtkinter
import socket
import threading
from tkinter import *
#----------------------------------------------------------------------------
# criar as funçoes para o teste ---------------------------------------------
def teste_conexao(endereco_ip, tentativas):
    for _ in range(tentativas):
        try:
            # Criar um socket e tentar se conectar ao endereço IP
            with socket.create_connection((endereco_ip, 80), timeout=5):
                LResultado.insert(END, "Conexão bem-sucedida")
                return
        except socket.error as e:
            # Em caso de erro, exibir a mensagem de erro na Listbox
            LResultado.insert(END, f"Erro na tentativa {_+1}: {e}")
    
    # Se todas as tentativas falharem, exibir mensagem de falha na Listbox
    LResultado.insert(END, "Não foi possível estabelecer uma conexão com o IP")

def teste_conexao_wrapper():
    # Limpar resultados anteriores
    LResultado.delete(0, END)
    
    # Obter o endereço IP da Entry
    endereco_ip = Eip.get()
    
    # Criar uma thread para realizar o teste de conexão
    thread = threading.Thread(target=teste_conexao, args=(endereco_ip, 4))
    thread.start()
#--------------------------------------------------------------------------

# defenir cores -----------------------------------------------------------
co0 = '#0000FF' # cor de fundo azul
co1 = '#FFFFFF' # cor de letra Branco 
#--------------------------------------------------------------------------

# Configuração da janela -------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('700x450+100+100')
Janela.resizable(False, False)
Janela.title('verifica Ligação(socket em Python Dev Joel)')
Janela.config(bg=co0)
Janela.iconbitmap(r'C:\Users\HP\Desktop\Teste Ligação a Internet\Icon.ico')
#-------------------------------------------------------------------------
# Criar um Label ---------------------------------------------------------
IP = Label(Janela, text='Endereço IP:', bg=co0,fg=co1,font=('arial 14'))
IP.place(x=0, y=10)
#-------------------------------------------------------------------------
# Criar a entry ----------------------------------------------------------
Eip = Entry(Janela, width=65, font=('arial 14'))
Eip.place(x=120, y=10)
#-------------------------------------------------------------------------
# Criar botão para teste de conexão --------------------------------------
B_criar = customtkinter.CTkButton(Janela, text='Teste Ligação', command=teste_conexao_wrapper, bg_color=co0)
B_criar.place(x=100, y=45)
#-------------------------------------------------------------------------
# Criar a listbox para resultados ----------------------------------------
LResultado = Listbox(Janela, width=75, height=18, font=('arial 14'))
LResultado.place(x=10, y=100)
#-------------------------------------------------------------------------
# Iniciar a janela -------------------------------------------------------
Janela.mainloop()
#-------------------------------------------------------------------------
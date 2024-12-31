import customtkinter as ctk
from tkinter import messagebox
from src import persistencia
from PIL import Image
import os

PASTA_IMGS = os.path.join(os.path.dirname(__file__), '..', 'assets', 'imgs')

def carregar_image_aluno():
    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    imagem = Image.open(caminho_foto)

    size = min(imagem.size)
    left = (imagem.width - size) // 2
    top = (imagem.height - size) // 2
    imagem_cortada = imagem.crop((left, top, left + size, top + size))
    
    
    return ctk.CTkImage(imagem_cortada, size=(200, 200))

def tela_exibir_alunos(root):

    #limpa a tela
    for widget in root.winfo_children():
        widget.pack_forget()
    
    #dimensões da tela
    root.configure(bg_color='#e5e3e3')
    root.update()

    width = root.winfo_width()
    height = root.winfo_height()

    #lista com os dados dos alunos
    alunos = list(persistencia.carregar_dados().get('alunos', []).values())

    max_colunas = len(alunos)

    foto_padrao = carregar_image_aluno()
   
    # Configuração do grid para ajustar o layout
    #linhas do root
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=1)

    #colunas do root
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)
    root.grid_columnconfigure(2, weight=1)

    #label escrito "alunos"
    label_alunos = ctk.CTkLabel(root, text='Alunos', font=('League Spartan', 80, 'bold'), text_color='#086a3d')
    label_alunos.grid(row=0, column=1, sticky='n', pady=50)

    #frame onde vai ficar os alunos
    frame_usuarios = ctk.CTkFrame(root, fg_color='#e5e3e3')
    frame_usuarios.configure(bg_color='#e5e3e3')
    frame_usuarios.grid(row=1, column=1, sticky='nsew')

    #configuração do layout do frame dos alunos
    #linhas
    frame_usuarios.grid_rowconfigure(0, weight=1)
    frame_usuarios.grid_rowconfigure(1, weight=1)
    frame_usuarios.grid_rowconfigure(2, weight=1)
    frame_usuarios.grid_rowconfigure(3, weight=1)

    #colunas
    for i, aluno in enumerate(alunos):
        frame_usuarios.grid_columnconfigure(i, weight=1)
    


        

    
    for i, aluno in enumerate(alunos):
        label_foto = ctk.CTkLabel(frame_usuarios, image=foto_padrao, text='')
        label_nome = ctk.CTkLabel(frame_usuarios, text=aluno['nome'], font=('League Spartan', 30, 'bold'), text_color='#3f3f3f')

        label_foto.grid(column=i, row=1, sticky='s')
        label_nome.grid(column=i, row=2, sticky='n')
        

def tela_cadastrar_aluno(root):
    print('cadastrar')
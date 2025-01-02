import customtkinter as ctk
from src import persistencia
from config import *
from src.views.menu import exibir_dashboard
from src.views import tools
import os

PASTA_IMGS = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'imgs')





def tela_exibir_alunos(root):
    
    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    foto_padrao = tools.criar_imagem_circular(caminho_foto)

    frame_principal = ctk.CTkFrame(root, fg_color=COR_BACKGROUND)
    frame_principal.place(relwidth=1, relheight=1)


    # Label escrito "Alunos"
    label_alunos = ctk.CTkLabel(frame_principal, text='Alunos', font=('League Spartan', 70, 'bold'), text_color=COR_VERDE)
    label_alunos.pack(pady=30)

    # Frame onde vai ficar os alunos
    frame_usuarios = ctk.CTkFrame(root, fg_color=COR_BACKGROUND)
    frame_usuarios.configure(bg_color=COR_BACKGROUND)
    frame_usuarios.place(rely=0.5, relx=0.5, anchor='center')

    # Configuração do layout do frame dos alunos
    # Linhas do frame de usuários
    frame_usuarios.grid_rowconfigure(0, weight=1)
    frame_usuarios.grid_rowconfigure(1, weight=1)
    frame_usuarios.grid_rowconfigure(2, weight=1)
    frame_usuarios.grid_rowconfigure(3, weight=1)

    dados = persistencia.carregar_dados()
    alunos = dados['alunos'].values()

    # Colunas do frame de usuários
    for i, aluno in enumerate(alunos):
        frame_usuarios.grid_columnconfigure(i, weight=1, minsize=180)  # Ajuste de largura mínima para as colunas

        label_foto = ctk.CTkLabel(frame_usuarios, image=foto_padrao, text='')
        label_foto.configure(cursor="hand2")

        label_foto.bind("<Button-1>", lambda event, aluno=aluno: exibir_dashboard.tela_exibir_dashboard(root, aluno, tools.criar_imagem_circular(caminho_foto, (80, 80))))

        label_nome = ctk.CTkLabel(
            frame_usuarios,
            text=aluno['nome'],
            font=('League Spartan', 25 , 'bold'),
            text_color='#3f3f3f',
            wraplength=180,  # Limita o texto a uma largura específica (180px)
            anchor="center"  # Garante que o texto fique centralizado
        )

        label_foto.grid(column=i, row=1)
        label_nome.grid(column=i, row=2, sticky='n', padx=5)  # Padding para evitar que o texto fique colado no limite

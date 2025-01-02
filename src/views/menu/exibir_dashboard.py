import customtkinter as ctk
from src.interface import limpar_root
from config import COR_BACKGROUND, COR_CINZA, COR_VERDE
from PIL import Image

def tela_exibir_dashboard(root, aluno, foto_perfil):
    root = limpar_root(root)

    # Configuração do grid para ajustar o layout
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)

    # Frame esquerdo ocupando toda a coluna 0
    frame_esquerdo = ctk.CTkFrame(root, fg_color=COR_VERDE, border_width=0, corner_radius=0)
    frame_esquerdo.grid(row=0, column=0, sticky='nsew')
    
    # Corrigindo o rowconfigure do frame_esquerdo
    for i in range(2):
        frame_esquerdo.rowconfigure(i, weight=5 if i > 0 else 1)  # Ajustando corretamente o peso das linhas
    frame_esquerdo.columnconfigure(0, weight=1)

    # Frame direito ocupando a coluna 1
    frame_direito = ctk.CTkFrame(root, fg_color=COR_BACKGROUND, border_width=0, corner_radius=0)
    frame_direito.grid(row=0, column=1, sticky='snew')

    # Frame onde vai ficar a foto perfil e o nome
    frame_perfil = ctk.CTkFrame(frame_esquerdo, fg_color=COR_VERDE,bg_color=COR_BACKGROUND, corner_radius=0, border_width=0)
    frame_perfil.grid(row=0, column=0, sticky='nsew')  # Ajustado o sticky para ocupar toda a área disponível

    # Ajustando o layout do frame_perfil

    frame_perfil.rowconfigure(0, weight=1)

    for i in range(3):
        frame_perfil.columnconfigure(i, weight=1)


    label_foto = ctk.CTkLabel(frame_perfil, image=foto_perfil, text='')
    label_foto.configure(cursor="hand2")

    label_foto.grid(row=0, column=1, sticky='n', pady=20)

    # Exibindo o nome do aluno centralizado no frame_perfil
    ctk.CTkLabel(frame_perfil, text=aluno['nome'], text_color=COR_BACKGROUND, font=('Arial', 22, 'bold')).grid(row=0, column=1, pady=100)

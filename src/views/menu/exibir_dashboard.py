import customtkinter as ctk
from src.interface import limpar_root
from config import COR_BACKGROUND, COR_CINZA, COR_VERDE



def tela_exibir_dashboard(root, aluno):

    root = limpar_root(root)
    
    # Configuração do grid para ajustar o layout
    # Linhas do root
    root.grid_rowconfigure(0, weight=1)

    # Colunas do root
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=5)

    # Frame esquerdo ocupando toda a coluna 0
    frame_esquerdo = ctk.CTkFrame(root, fg_color=COR_VERDE, border_width=0)
    frame_esquerdo.grid(row=0, column=0, sticky='nsew')  # 'nsew' faz o frame ocupar todo o espaço disponível

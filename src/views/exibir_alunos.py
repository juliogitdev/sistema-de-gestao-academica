import customtkinter as ctk
from src import persistencia
from PIL import Image
from src.views.menu import exibir_dashboard
import os

PASTA_IMGS = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'imgs')

def carregar_image_aluno():
    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    imagem = Image.open(caminho_foto)

    size = min(imagem.size)
    left = (imagem.width - size) // 2
    top = (imagem.height - size) // 2
    imagem_cortada = imagem.crop((left, top, left + size, top + size))

    return ctk.CTkImage(imagem_cortada, size=(180, 180))



def tela_exibir_alunos(root):
    # Limpa a tela
    for widget in root.winfo_children():
        widget.pack_forget()


    root.configure(bg_color='#e5e3e3')
    root.update()

    width = root.winfo_width()
    height = root.winfo_height()

    # Lista com os dados dos alunos
    alunos = list(persistencia.carregar_dados().get('alunos', []).values())

    # Número máximo de colunas
    max_colunas = len(alunos)

    foto_padrao = carregar_image_aluno()

    # Configuração do grid para ajustar o layout
    # Linhas do root
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=1)

    # Colunas do root
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)
    root.grid_columnconfigure(2, weight=1)

    # Label escrito "Alunos"
    label_alunos = ctk.CTkLabel(root, text='Alunos', font=('League Spartan', 70, 'bold'), text_color='#086a3d')
    label_alunos.grid(row=0, column=1, sticky='n', pady=50)

    # Frame onde vai ficar os alunos
    frame_usuarios = ctk.CTkFrame(root, fg_color='#e5e3e3')
    frame_usuarios.configure(bg_color='#e5e3e3')
    frame_usuarios.grid(row=1, column=1, sticky='nsew')

    # Configuração do layout do frame dos alunos
    # Linhas do frame de usuários
    frame_usuarios.grid_rowconfigure(0, weight=1)
    frame_usuarios.grid_rowconfigure(1, weight=1)
    frame_usuarios.grid_rowconfigure(2, weight=1)
    frame_usuarios.grid_rowconfigure(3, weight=1)

    # Colunas do frame de usuários
    for i, aluno in enumerate(alunos):
        frame_usuarios.grid_columnconfigure(i, weight=1, minsize=180)  # Ajuste de largura mínima para as colunas

        label_foto = ctk.CTkLabel(frame_usuarios, image=foto_padrao, text='')
        label_foto.configure(cursor="hand2")

        label_foto.bind("<Button-1>", lambda event, aluno=aluno: exibir_dashboard.tela_exibir_dashboard(root, aluno))

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

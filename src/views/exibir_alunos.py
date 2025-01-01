import customtkinter as ctk
from src import persistencia
from PIL import Image, ImageTk, ImageDraw
from src.views.menu import exibir_dashboard
import os

PASTA_IMGS = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'imgs')


# Função para recortar a imagem em formato circular
def criar_imagem_circular(caminho_imagem, tamanho=(180, 180)):
    # Abrir a imagem
    imagem = Image.open(caminho_imagem)

    # Calcular o menor lado para criar um quadrado central
    lado_menor = min(imagem.size)
    esquerda = (imagem.width - lado_menor) // 2
    topo = (imagem.height - lado_menor) // 2
    direita = esquerda + lado_menor
    inferior = topo + lado_menor

    # Cortar a imagem para um quadrado central
    imagem = imagem.crop((esquerda, topo, direita, inferior))

    # Redimensionar para o tamanho desejado
    imagem = imagem.resize(tamanho, Image.LANCZOS)

    # Criar a máscara circular
    mascara = Image.new("L", tamanho, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, tamanho[0], tamanho[1]), fill=255)

    # Aplicar a máscara na imagem
    imagem_circular = Image.new("RGBA", tamanho, (0, 0, 0, 0))
    imagem_circular.paste(imagem, (0, 0), mask=mascara)

    # Converter para CTkImage
    return ctk.CTkImage(light_image=imagem_circular, size=tamanho)


"""
def carregar_image_aluno():
    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    imagem = Image.open(caminho_foto)

    size = min(imagem.size)
    left = (imagem.width - size) // 2
    top = (imagem.height - size) // 2
    imagem_cortada = imagem.crop((left, top, left + size, top + size))
"""



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

    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    foto_padrao = criar_imagem_circular(caminho_foto)

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

        label_foto.bind("<Button-1>", lambda event, aluno=aluno: exibir_dashboard.tela_exibir_dashboard(root, aluno, foto_padrao))

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

import customtkinter as ctk
from src import persistencia
from PIL import Image,ImageDraw
from config import *
from src.views.menu import exibir_dashboard
import os

PASTA_IMGS = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'imgs')


# Função para recortar a imagem em formato circular
def criar_imagem_circular(caminho_imagem, tamanho=(120, 120)):
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


def tela_exibir_alunos(root):
    
    caminho_foto = os.path.join(PASTA_IMGS, 'login.jpg')
    foto_padrao = criar_imagem_circular(caminho_foto)

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

        label_foto.bind("<Button-1>", lambda event, aluno=aluno: exibir_dashboard.tela_exibir_dashboard(root, aluno, criar_imagem_circular(caminho_foto, (100, 100))))

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

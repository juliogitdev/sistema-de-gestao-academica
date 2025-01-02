import customtkinter as ctk
from src.interface import limpar_root
from config import COR_BACKGROUND, COR_CINZA, COR_VERDE
from PIL import Image, ImageDraw
from src.views.menu import cadastrar_curso, cadastrar_disciplina, cadastrar_nota, desempenho, historico
from src.views import tools
import os
import time

foto_perfil_caminho = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'assets', 'imgs', 'login.jpg')

# Variável para controle do debounce
last_resize_time = 0

def ajustar_textos_botoes(root, menu_buttons, foto_perfil, label_image_perfil, nome_perfil):
    global last_resize_time
    
    # Impede a execução da função durante o redimensionamento contínuo
    current_time = time.time()
    if current_time - last_resize_time < 0.2:  # Delay de 200ms entre redimensionamentos
        return
    last_resize_time = current_time

    # Calculando o tamanho da fonte com base na largura da janela
    largura_janela = root.winfo_width()
    novo_tamanho_fonte = int(largura_janela // 80)

    # Atualizando o tamanho da fonte de cada botão
    for button in menu_buttons:
        button.configure(font=('Impact', novo_tamanho_fonte))

    # Ajustando a imagem do perfil
    novo_tamanho_imagem = int(largura_janela // 10)  # A imagem será 1/10 da largura da janela
    nova_imagem = tools.criar_imagem_circular(foto_perfil_caminho, (novo_tamanho_imagem, novo_tamanho_imagem))

    # Atualizando a imagem do perfil
    label_image_perfil.configure(image=nova_imagem)
    label_image_perfil.image = nova_imagem  # Para evitar que a imagem seja recolocada pelo garbage collector

    # Atualizando tamanho nome perfil
    nome_perfil.configure(font=('Arial', int(largura_janela * 0.020), 'bold'))  # Corrigindo o cálculo do tamanho da fonte

def tela_exibir_dashboard(root, aluno, foto_perfil):
    root = limpar_root(root)

    # Configurando frame principal
    frame_principal = ctk.CTkFrame(root, fg_color=COR_BACKGROUND)
    frame_principal.place(relwidth=1, relheight=1)

    # Configurando o frame esquerdo
    frame_esquerdo = ctk.CTkFrame(frame_principal, fg_color=COR_VERDE, bg_color=COR_BACKGROUND, corner_radius=0)
    frame_esquerdo.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    # Configurando o frame direito
    frame_direito = ctk.CTkFrame(frame_principal, fg_color=COR_BACKGROUND, bg_color=COR_BACKGROUND)
    frame_direito.place(relx=0.8, rely=0, relwidth=0.8, relheight=1)

    # Frame onde vai ficar a foto e o nome do perfil
    frame_perfil = ctk.CTkFrame(frame_esquerdo, fg_color=COR_VERDE, corner_radius=0)
    frame_perfil.pack(side='top', fill='x', pady=20)

    # Foto perfil (passando a imagem já criada)
    label_image_perfil = ctk.CTkLabel(frame_perfil, text='', image=foto_perfil)
    label_image_perfil.pack(pady=10, expand=True)

    # Nome do aluno
    nome_aluno = ctk.CTkLabel(frame_perfil, text=aluno['nome'], font=('Arial', 22, 'bold'), text_color=COR_BACKGROUND)
    nome_aluno.pack(expand=True)

    menu = {
        'CURSOS': cadastrar_curso.tela_cadastrar_curso(),
        'CADASTRAR NOTA': cadastrar_nota.tela_cadastrar_nota(),
        'CADASTRAR DISCIPLINA': cadastrar_disciplina.tela_cadastrar_disciplina(),
        'HISTÓRICO': historico.tela_historico(),
        'DESEMPENHO': desempenho.tela_exibir_desempenho()
    }

    menu_buttons = []
    
    frame_menu = ctk.CTkFrame(frame_esquerdo, fg_color=COR_VERDE)
    frame_menu.pack(fill="x", expand=True)
    for option in menu.keys():
        button = ctk.CTkButton(frame_menu,
        fg_color=COR_VERDE,
        bg_color=COR_VERDE,
        border_color=COR_VERDE,
        corner_radius=0,
        height=60,
        font=('Impact', 16, 'bold'), 
        anchor='center',
        text=option, 
        cursor='hand2',)

        button.pack(pady=1, fill='x')

        menu_buttons.append(button)
    
    # Chama a função de ajuste de textos quando a tela for redimensionada
    root.bind('<Configure>', lambda event: ajustar_textos_botoes(root, menu_buttons, foto_perfil, label_image_perfil, nome_aluno))

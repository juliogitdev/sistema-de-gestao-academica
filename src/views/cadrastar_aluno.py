import customtkinter as ctk
from config import *
from src import interface, persistencia
from tkinter import messagebox
from src.views import exibir_alunos
import re

def verificar_entradas(matricula, nome, root):

    # Verifica se a matrícula é numérica
    if not matricula.isdigit():
        messagebox.showinfo('Alerta', 'A matrícula deve ser apenas números!')
        return
    
    # Verifica se a matrícula tem 12 dígitos
    if len(matricula) != 12:
        messagebox.showinfo('Alerta', "A matrícula deve ter 12 dígitos!")
        return
    
    # Verifica se o nome é uma string não vazia e só contém letras e espaços
    if not nome or not nome.strip():
        messagebox.showinfo('Alerta', 'Nome inválido')
        return
    
    if not re.match("^[A-Za-z\\s]*$", nome):
        messagebox.showinfo('Alerta', 'O nome deve conter apenas letras e espaços!')
        return
    
    cadastro = persistencia.adicionar_matricula(nome, matricula)

    if cadastro:
        messagebox.showinfo('Parabéns', 'Dados cadastrados')
    else:
        messagebox.showinfo('Alerta', 'Matrícula já cadastrada')
        return



def exibir_tela_cadastrar_aluno(root):
    frame_esquerdo = ctk.CTkFrame(root, fg_color=COR_VERDE, corner_radius=0)
    frame_esquerdo.place(relwidth=0.3, relheight=1)

    frame_direito = ctk.CTkFrame(root, fg_color=COR_BACKGROUND, corner_radius=0)
    frame_direito.place(relwidth=0.7, relheight=1, relx=0.3)

    frame_itens_esquerda = ctk.CTkFrame(frame_esquerdo, fg_color=COR_VERDE, corner_radius=0)
    frame_itens_esquerda.place(relwidth=1, rely=0.5, anchor='w')

    text_bem_vindo = ctk.CTkLabel(frame_itens_esquerda, text='Bem-vindo!', font=('Arial', 40, 'bold'), text_color=COR_BACKGROUND)
    text_bem_vindo.pack()

    text_descricao = ctk.CTkLabel(
        frame_itens_esquerda, 
        text='Gerencie suas disciplinas, notas e desempenho acadêmico aqui.', 
        font=('Arial', 18), 
        text_color=COR_BACKGROUND,
        wraplength=200
    )
    text_descricao.pack()

    frame_itens_direita = ctk.CTkFrame(frame_direito, fg_color=COR_BACKGROUND, corner_radius=0)
    frame_itens_direita.place(relx=0.5, rely=0.5, relwidth=0.8, anchor='center')
    label_cadastrar_aluno = ctk.CTkLabel(
        frame_itens_direita, 
        text="CRIAR PERFIL", 
        font=('League Spartan', 40, 'bold'),
        text_color=COR_VERDE
    )
    label_cadastrar_aluno.pack(pady=10, fill="both", expand=True)

    input_matricula = ctk.CTkEntry(frame_itens_direita, fg_color=COR_CINZA, placeholder_text='Matrícula', width=250, height=50,
                 corner_radius=15, placeholder_text_color=COR_BACKGROUND, font=('League Spartan', 20),
                 border_width=0)
    
    input_matricula.pack(pady=10)
    
    input_nome = ctk.CTkEntry(frame_itens_direita, fg_color=COR_CINZA, placeholder_text='Nome', width=250, height=50,
                 corner_radius=15, placeholder_text_color=COR_BACKGROUND, font=('League Spartan', 20),
                 border_width=0)

    input_nome.pack()

    botao_criar = ctk.CTkButton(
        frame_itens_direita,
        width=200, 
        height=50,
        corner_radius=15, 
        fg_color=COR_VERDE,
        font=('League Spartan', 25, 'bold'), 
        anchor='center', 
        text='Criar', 
        cursor='hand2', 
        command= lambda: verificar_entradas(input_matricula.get(), input_nome.get(), root))
    
    botao_criar.pack(pady=20)



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
    
    if not re.match("^[A-Za-z\s]*$", nome):
        messagebox.showinfo('Alerta', 'O nome deve conter apenas letras e espaços!')
        return
    
    cadastro = persistencia.adicionar_matricula(nome, matricula)

    if cadastro:
        messagebox.showinfo('Parabéns', 'Dados cadastrados')
    else:
        messagebox.showinfo('Alerta', 'Matrícula já cadastrada')
        return
    

    


def exibir_tela_cadastrar_aluno(root):
    # Limpa a tela
    for widget in root.winfo_children():
        widget.pack_forget()

    root.configure(bg_color=COR_BACKGROUND)
    root.update()

    backup_frame_root = root

    # Layout principal
    root.grid_columnconfigure([0, 1], weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_rowconfigure(0, weight=1)

    # Frame esquerdo
    frame_esquerdo = ctk.CTkFrame(root, fg_color=COR_VERDE)
    frame_esquerdo.grid(column=0, sticky='snew')
    frame_esquerdo.grid_rowconfigure([0, 1, 2], weight=1)
    frame_esquerdo.grid_columnconfigure(0, weight=1)

    frame_texto_boas_vindas = ctk.CTkFrame(frame_esquerdo, fg_color=COR_VERDE, corner_radius=0)
    frame_texto_boas_vindas.grid(row=1, column=0)
    frame_texto_boas_vindas.grid_rowconfigure([0, 1], weight=1)
    frame_texto_boas_vindas.grid_columnconfigure(0, weight=1)

    #Texto Bem vindo do lado esquerdo
    ctk.CTkLabel(frame_texto_boas_vindas, text="Bem-vindo!", font=('League Spartan', 40, 'bold'),
                 anchor="center", text_color='white').grid(row=0, column=0, sticky='s')

    ctk.CTkLabel(frame_texto_boas_vindas,
                 text="Gerencie suas disciplinas, notas e desempenho acadêmico aqui.",
                 font=('League Spartan', 16), wraplength=250).grid(row=1, column=0, sticky='n', pady=10)

    # Frame direito
    frame_direito = ctk.CTkFrame(root, fg_color=COR_BACKGROUND)
    frame_direito.grid(column=1, row=0, sticky='snew')

    #criando as linhas do frame direito
    for i in range(5):
        frame_direito.grid_rowconfigure(i, weight=1)

    frame_direito.grid_columnconfigure([0, 2], weight=1)
    frame_direito.grid_columnconfigure(1, weight=2)

    ctk.CTkLabel(frame_direito, text="CRIAR PERFIL", font=('League Spartan', 40, 'bold'),
                 anchor="center", text_color=COR_VERDE).grid(column=1, row=1, sticky='s')

    #Crinando o frame onde irá ficar as entradas. (Matricula, nome)
    frame_input = ctk.CTkFrame(frame_direito, fg_color=COR_BACKGROUND)
    frame_input.grid(column=1, row=2, sticky='snew')

    #configurando a grade do frame onde irá ficar as entradas
    frame_input.grid_rowconfigure([0, 1], weight=1)
    frame_input.grid_columnconfigure(0, weight=1)

    input_matricula = ctk.CTkEntry(frame_input, fg_color=COR_CINZA, placeholder_text='Matrícula', width=250, height=50,
                 corner_radius=15, placeholder_text_color=COR_BACKGROUND, font=('League Spartan', 20),
                 border_width=0)
    input_matricula.grid(column=0, row=0, sticky='s')

    input_nome = ctk.CTkEntry(frame_input, fg_color=COR_CINZA, placeholder_text='Nome', width=250, height=50,
                 corner_radius=15, placeholder_text_color=COR_BACKGROUND, font=('League Spartan', 20),
                 border_width=0)
    input_nome.grid(column=0, row=1)

    botao_criar = ctk.CTkButton(frame_direito, width=200, height=50, corner_radius=15, fg_color=COR_VERDE,
                  font=('League Spartan', 25, 'bold'), anchor='center', text='Criar', cursor='hand2', command= lambda: verificar_entradas(input_matricula.get(), input_nome.get(), root)).grid(column=1, row=3, sticky='n')
    

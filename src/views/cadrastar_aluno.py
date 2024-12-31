import customtkinter as ctk





def exibir_tela_cadastrar_aluno(root):
    # Limpa a tela
    for widget in root.winfo_children():
        widget.pack_forget()

    root.configure(bg_color='#e5e3e3')
    root.update()

    #dividindo o layout em duas colunas
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_rowconfigure(0, weight=1)

    #root.bind('<Configure>', ajustar_items)

    #criando e configurando frame esquerdo
    frame_esquerdo = ctk.CTkFrame(root, fg_color='#086a3d')
    frame_esquerdo.grid(column=0, sticky='snew')

    frame_esquerdo.grid_rowconfigure(0, weight=1)
    frame_esquerdo.grid_rowconfigure(1, weight=1)
    frame_esquerdo.grid_rowconfigure(2, weight=1)

    frame_esquerdo.grid_columnconfigure(0, weight=1)

    frame_texto_boas_vindas = ctk.CTkFrame(frame_esquerdo, fg_color='#086a3d', corner_radius=0)
    frame_texto_boas_vindas.grid(row=1, column=0)

    frame_texto_boas_vindas.grid_columnconfigure(0, weight=1)

    frame_texto_boas_vindas.grid_rowconfigure(0, weight=1)
    frame_texto_boas_vindas.grid_rowconfigure(1, weight=1)

    label_bem_vindo = ctk.CTkLabel(frame_texto_boas_vindas, text="Bem-vindo!",font=('League Spartan', 40, 'bold'), anchor="center", text_color='white')
    label_descricao = ctk.CTkLabel(frame_texto_boas_vindas,
                                   text="Gerencie suas disciplinas, notas e desempenho acadêmico aqui.",
                                   font=('League Spartan', 16), wraplength=250)

    label_bem_vindo.grid_configure(row=0, column=0, sticky='s')
    label_descricao.grid_configure(row=1, column=0, sticky='n', pady=10)

    #Criando e configurando frame direito

    frame_direito = ctk.CTkFrame(root, fg_color='#e5e3e3')
    frame_direito.grid(column=1, row=0, sticky='snew')

    frame_direito.rowconfigure(0, weight=1)
    frame_direito.rowconfigure(1, weight=1)
    frame_direito.rowconfigure(2, weight=1)
    frame_direito.rowconfigure(3, weight=1)
    frame_direito.rowconfigure(4, weight=1)

    frame_direito.columnconfigure(0, weight=1)
    frame_direito.columnconfigure(1, weight=2)
    frame_direito.columnconfigure(2, weight=1)

    label_criar_perfil = ctk.CTkLabel(frame_direito, text="CRIAR PERFIL",font=('League Spartan', 40, 'bold'), anchor="center", text_color='#086a3d')
    label_criar_perfil.grid(column=1, row=1, sticky='s')

    frame_input = ctk.CTkFrame(frame_direito, fg_color='#e5e3e3')

    frame_input.rowconfigure(0, weight=1)
    frame_input.rowconfigure(1, weight=1)

    frame_input.columnconfigure(0, weight=1)

    frame_input.grid(column=1, row=2, sticky='snew')

    input_matricula = ctk.CTkEntry(frame_input, fg_color='#a6a6a6', placeholder_text='Matrícula', width=250, height=50, corner_radius=15, placeholder_text_color='#e5e3e3', font=('League Spartan', 20), border_width=0)
    input_matricula.grid(column=0, row=0, sticky='s')
    input_nome = ctk.CTkEntry(frame_input, fg_color='#a6a6a6', placeholder_text='Nome', width=250, height=50, corner_radius=15, placeholder_text_color='#e5e3e3', font=('League Spartan', 20), border_width=0)
    input_nome.grid(column=0, row=1)
    
    botao_criar = ctk.CTkButton(frame_direito, width=200, height=50, corner_radius=15, fg_color='#086a3d', font=('League Spartan', 25, 'bold'), anchor='center', text='Criar')
    botao_criar.grid(column=1, row=3, sticky='n')
    botao_criar.configure(cursor='hand2')
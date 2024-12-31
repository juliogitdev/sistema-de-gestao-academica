import customtkinter as ctk
from src import interface, persistencia


def main():
    root = ctk.CTk()
    root.title("Gerenciador")
    root.geometry("800x600")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame_principal = ctk.CTkFrame(root, fg_color='#e5e3e3')
    frame_principal.grid(row=0, column=0, sticky='snew')
    
    if len(persistencia.carregar_dados()['alunos']) > 0:
        interface.tela_exibir_alunos(frame_principal)
        
    else:
        interface.tela_cadastrar_aluno(frame_principal)

    root.mainloop()

if __name__ == "__main__":
    main()

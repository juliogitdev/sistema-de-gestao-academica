import customtkinter as ctk
from src import interface, persistencia


def main():
    root = ctk.CTk()
    root.title("Gerenciador")
    root.geometry("800x600")
    
    if len(persistencia.carregar_dados()['alunos']) > 0:
        interface.mostrar_usuario()
    else:
        interface.cadastrar_usuario()

    root.mainloop()

if __name__ == "__main__":
    main()

import customtkinter as ctk
from src import interface, persistencia
from src.views import cadrastar_aluno, exibir_alunos
from src.views.menu import cadastrar_curso, cadastrar_disciplina, cadastrar_nota, desempenho, exibir_dashboard, historico


def main():
    root = ctk.CTk()
    root.title("Gerenciador")
    root.geometry("800x600")

    if len(persistencia.carregar_dados()['alunos']) > 0:
        exibir_alunos.tela_exibir_alunos(root)
    else:
        cadrastar_aluno.exibir_tela_cadastrar_aluno(root)
        

    root.mainloop()

if __name__ == "__main__":
    main()

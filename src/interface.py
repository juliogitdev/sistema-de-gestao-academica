from src.views import exibir_alunos, cadrastar_aluno

COR_BACKGROUND = '#e5e3e3'
COR_VERDE = '#086a3d'
COR_CINZA = '#a6a6a6'

def mudar_tela(root, tela_nova):
    # Limpa todos os widgets da tela atual
    for widget in root.winfo_children():
        widget.grid_forget()
    
    # Exibe a nova tela
    tela_nova(root)

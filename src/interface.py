from src.views import exibir_alunos, cadrastar_aluno

COR_BACKGROUND = '#e5e3e3'
COR_VERDE = '#086a3d'
COR_CINZA = '#a6a6a6'

def tela_exibir_alunos(root):
    exibir_alunos.tela_exibir_alunos(root)

def tela_cadastrar_aluno(root):
    cadrastar_aluno.exibir_tela_cadastrar_aluno(root)
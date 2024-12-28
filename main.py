from src import api_integration
from src import interface
from src import persistencia

def main():
    matriculas = persistencia.obter_matriculas()
    dados = persistencia.carregar_dados()

    #Verificar se existe algum perfil
    if matriculas:
        print("Perfis disponíveis:")
        #pecorrendo por todos perfis cadastrados e imprimindo o nome
        for matricula in matriculas:
            aluno = dados['alunos'][matricula]['nome']
            print(aluno)
        
        #chamar a interface de selecionar perfil
    
    #Caso não exista perfil criado
    else:
        print("Nenhum perfil criado.")
        #chama a interface de criar perfil

if __name__ == "__main__":
    main()
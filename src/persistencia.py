import os
import json

# Caminho do arquivo JSON
caminho_arquivo_json = os.path.join(os.path.dirname(__file__),'..', 'data', 'data.json')


#Retorna os dados do arquivo json
def carregar_dados():

    if os.path.exists(caminho_arquivo_json):

        try:
            with open(caminho_arquivo_json, 'r', encoding='utf-8') as dados:
                return json.load(dados)
            
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            return {}
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return {}
    else:
        print("Arquivo não encontrado!")
        return {}  # Retorna um dicionário vazio se o arquivo não for encontrado


def obter_matriculas():
    dados = carregar_dados()

    return list(dados.get('alunos', {}).keys())
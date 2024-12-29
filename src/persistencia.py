import os
import json
import hashlib


# Caminho do arquivo JSON
caminho_arquivo_json = os.path.join(os.path.dirname(__file__),'..', 'data', 'data.json')

# Função para gerar um hash único para o ID da disciplina
def gerar_id_com_hash(disciplina, id_curso):
    # Combina o nome da disciplina com o ID do curso para criar uma string única
    texto = disciplina + str(id_curso)
    # Gera o hash dessa string única usando o algoritmo SHA256
    hash_object = hashlib.sha256(texto.encode())
    
    # Pegamos os primeiros 8 caracteres do hash gerado para usar como ID
    id_hash = hash_object.hexdigest()[:4]
    
    return id_hash


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



#retorna todas as matriculas cadastradas
def obter_matriculas():
    dados = carregar_dados()

    return list(dados.get('alunos', {}).keys())


#salva os dados json
def salvar_dados(dados):
    try:
        with open(caminho_arquivo_json, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            print("dados salvos com sucesso")
    except Exception as e:
        print(f"Erro ao salvar os dados. erro: {e}")


#Adiciona um perfil
def adicionar_matricula(nome, matricula):
    dados = carregar_dados()

    if not matricula in dados['alunos']:
        dados['alunos'][matricula] = {"nome": nome, "cursos":[], "disciplinas": []}
        salvar_dados(dados)
    else:
        print(f"A matrícula {matricula} já existe.")

#Excluir perfil
def remover_matricula(matricula):
    dados = carregar_dados()

    if matricula in dados['alunos']:
        del dados['alunos'][matricula]
        del dados['notas'][matricula]
        salvar_dados(dados)
    
    else:
        print("Matrícula não cadastrada ou inválida")

#retorna todas as disciplinas criadas
def listar_disciplinas():
    dados = carregar_dados()
    return dados.get('disciplinas', [])

# Função para adicionar uma nova disciplina com ID gerado por hash
def adicionar_disciplina(nome_disciplina, id_curso):
    dados = carregar_dados()

    id = gerar_id_com_hash(nome_disciplina, id_curso)

    # Verificar se a disciplina já existe para o mesmo curso
    for disciplina in dados['disciplinas']:
        if id == disciplina['id'] and disciplina['id_curso'] == id_curso:
            return print(f"A disciplina '{nome_disciplina}' já existe no curso com ID {id_curso}.")

    nova_disciplina = {"id": id, "nome": nome_disciplina, "id_curso": id_curso}

    # Adicionar a nova disciplina
    dados['disciplinas'].append(nova_disciplina)

    # Salvar os dados de volta no arquivo JSON
    salvar_dados(dados)

    print(f"Disciplina '{nome_disciplina}' adicionada com ID {id} no curso {id_curso}.")



def remover_disciplina(id_disciplina):
    dados = carregar_dados()

    # Verificar se a disciplina está associada a algum aluno
    for aluno in dados['alunos'].values():
        if any(d['id'] == id_disciplina for d in aluno['disciplinas']):
            print("A disciplina está associada a um aluno e não pode ser removida.")
            return

    # Se não estiver associada a nenhum aluno, removê-la
    dados['disciplinas'] = [d for d in dados['disciplinas'] if d['id'] != id_disciplina]
    salvar_dados(dados)
    print(f"Disciplina com ID {id_disciplina} removida com sucesso.")


def manipular_notas(matricula, semestre, id_disciplina, nota1, nota2, editar=False):
    dados = carregar_dados()

    # Calcular a média ponderada
    media = (nota1 + nota2) / 2

    # Estrutura para as notas
    nota_info = {
        "id_disciplina": id_disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
    }

    # Verificar se a matrícula existe no dicionário de notas
    if matricula not in dados['notas']:
        print(f"A matrícula {matricula} não existe.")
        return

    # Verificar se o semestre existe para a matrícula
    if semestre not in dados['notas'][matricula]:
        print(f"O semestre {semestre} não foi encontrado para a matrícula {matricula}.")
        return

    # Se editar, procuramos pela disciplina e substituímos as notas
    if editar:
        disciplina_encontrada = False
        for idx, nota in enumerate(dados['notas'][matricula][semestre]):
            if nota['id_disciplina'] == id_disciplina:
                # Substituir as notas e atualizar a média
                dados['notas'][matricula][semestre][idx] = nota_info
                disciplina_encontrada = True
                salvar_dados(dados)
                print(f"Notas para a disciplina {id_disciplina} do aluno {matricula} no semestre {semestre} atualizadas com sucesso.")
                break

        if not disciplina_encontrada:
            print(f"Disciplina {id_disciplina} não encontrada para o aluno {matricula} no semestre {semestre}.")
        return

    # Se não for edição, adicionamos as notas para a disciplina
    dados['notas'][matricula][semestre].append(nota_info)
    
    # Salvar os dados no arquivo JSON
    salvar_dados(dados)
    
    print(f"Notas para a disciplina {id_disciplina} adicionadas com sucesso ao aluno {matricula} no semestre {semestre}.")

def adicionar_curso_a_aluno(matricula, id_curso):
    dados = carregar_dados()

    if not matricula in dados['alunos']:
        print(f"Matrícula inválida. {matricula}")
        return
    
    if id_curso in dados['alunos'][matricula]['cursos']:
        print(f"O curso {id_curso} já está associado ao {matricula}")
        return
    
    dados['alunos'][matricula]['cursos'].append(id_curso)
    salvar_dados(dados)


def remover_curso_de_aluno(matricula, id_curso):
    dados = carregar_dados()

    # Verificar se o aluno existe
    if matricula not in dados['alunos']:
        print(f"A matrícula {matricula} não foi encontrada.")
        return

    # Verificar se o curso está associado ao aluno
    if id_curso not in dados['alunos'][matricula]['cursos']:
        print(f"O curso {id_curso} não está associado ao aluno {matricula}.")
        return

    # Remover o curso da lista de cursos do aluno
    dados['alunos'][matricula]['cursos'].remove(id_curso)

    # Remover as disciplinas relacionadas ao curso
    disciplinas_removidas = []
    for disciplina in list(dados['alunos'][matricula]['disciplinas']):
        for d in dados['disciplinas']:
            if d['id'] == disciplina and d['id_curso'] == id_curso:
                dados['alunos'][matricula]['disciplinas'].remove(disciplina)
                disciplinas_removidas.append(disciplina)

    # Remover notas relacionadas às disciplinas do curso
    if matricula in dados['notas']:
        for semestre in list(dados['notas'][matricula].keys()):
            dados['notas'][matricula][semestre] = [
                nota for nota in dados['notas'][matricula][semestre]
                if nota['id_disciplina'] not in disciplinas_removidas
            ]
            # Remover semestre vazio, se necessário
            if not dados['notas'][matricula][semestre]:
                del dados['notas'][matricula][semestre]

    # Salvar as alterações
    salvar_dados(dados)



def adicionar_disciplina_a_aluno(matricula, id_disciplina):
    dados = carregar_dados()
    #verifica se o número da matricula está em alunos

    if not matricula in dados['alunos']:
        print("Matricula inválida.")
        return

    #verifica se a disciplina não está a associada ao aluno
    if id_disciplina in dados['alunos'][matricula]['disciplinas']:
        print("Já está associado a está disciplina")
        return
    
    for dado in dados['disciplinas']:

    #verifica se o id da disciplina é válido
        if dado['id'] == id_disciplina:
            dados['alunos'][matricula]['disciplinas'].append(id_disciplina)
            salvar_dados(dados)
            return
    
    print("Disciplina inválido")
    
def remover_disciplina_de_aluno(matricula, id_disciplina):
    dados = carregar_dados()

    # Verificar se o aluno existe
    if matricula not in dados['alunos']:
        print(f"A matrícula {matricula} não existe.")
        return

    aluno = dados['alunos'][matricula]

    # Verificar se a disciplina está associada ao aluno
    if id_disciplina not in [d['id'] for d in aluno['disciplinas']]:
        print(f"A disciplina com ID {id_disciplina} não está associada ao aluno {matricula}.")
        return

    # Remover a disciplina do aluno
    aluno['disciplinas'] = [d for d in aluno['disciplinas'] if d['id'] != id_disciplina]

    # Remover as notas associadas à disciplina do aluno
    if matricula in dados['notas']:
        for semestre in dados['notas'][matricula]:
            dados['notas'][matricula][semestre] = [nota for nota in dados['notas'][matricula][semestre] if nota['id_disciplina'] != id_disciplina]

    # Salvar os dados após a remoção
    salvar_dados(dados)

    print(f"A disciplina com ID {id_disciplina} foi removida do aluno {matricula} e suas notas excluídas.")


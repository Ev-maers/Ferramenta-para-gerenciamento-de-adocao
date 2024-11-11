import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def carregar_dados():
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(dados):
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4)


def gerar_id_unico(dados):
    if not dados:
        return 1  
    else:
        maior_id = max(voluntario["id"] for voluntario in dados)
        return maior_id + 1

def adicionar_voluntario(nome, idade, email, contato):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados) 
    novo_voluntario = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "contato": email,
        "celular": contato  
    }
    dados.append(novo_voluntario)
    salvar_dados(dados)
    print(f"voluntario adicionado com sucesso! ID: {novo_id}")

def listar_animais():
    dados = carregar_dados()
    if not dados: 
        print("Nenhum voluntario encontrado.")
        return
    for voluntario in dados:
        print(f"ID: {voluntario['id']} - Nome: {voluntario['nome']}, Idade: {voluntario['idade']}, email: {voluntario['email']}, Contato: {voluntario['contato']}")

def atualizar_voluntario(id, novo_nome, nova_idade, novo_email, novo_contato):
    dados = carregar_dados()
    for voluntario in dados:
        if voluntario["id"] == id:
            voluntario["nome"] = novo_nome
            voluntario["idade"] = nova_idade
            voluntario["contato"] = novo_email
            voluntario["celular"] = novo_contato
            salvar_dados(dados)
            print("Voluntário atualizado com sucesso!")
            return
    print("Voluntário não encontrado.")

def deletar_voluntario(id):
    dados = carregar_dados()
    dados = [voluntario for voluntario in dados if voluntario["id"] != id]
    salvar_dados(dados)
    print("Voluntário removido com sucesso!")
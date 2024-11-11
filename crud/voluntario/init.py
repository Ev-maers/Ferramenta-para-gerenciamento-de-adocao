from voluntario.operations import adicionar_voluntario, listar_voluntarios, atualizar_voluntario, deletar_voluntario
def menu_voluntario():
    print("===== Gerenciamento de voluntários =====")
    print("1. Adicionar voluntário")
    print("2. Lista dos voluntários")
    print("3. Atualizar um voluntário")
    print("4. Remover voluntário")
    print("5. Voltar ao Menu Principal")

def main():
    while True:
        menu_voluntario()
        op = input("Escolha a opção: ")

        if op == '1':
            nome = input("Informe o nome e sobrenome do voluntário: ")
            idade = int(input("Informe a idade da pessoa? "))
            email = input("Informe um email para contato: ")
            contato = input("Informe um número para contado, conforme o exemplo (DDD) 9 0000-0000: ")
            adicionar_voluntario(nome, idade, email, contato)

        elif op == '2':
            listar_voluntarios()

        elif op == '3':
            id = int(input("Digite o ID do voluntario a ser atualizado: "))
            novo_nome = input("Digite o novo nome do voluntario: ")
            novo_email = input("Digite a nova personalidade do voluntario: ")
            nova_contato = input("Digite a nova situação de saúde do voluntario: ")
            atualizar_voluntario(id, novo_nome, nova_idade, novo_email, novo_contato)

        elif op == '4':
            id = int(input("Digite o ID do voluntario a ser deletado: "))
            deletar_voluntario(id)

        elif op == '5':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")
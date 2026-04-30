opcao = 0
dados = []

def menu():
    print("\nEscolha uma das opções abaixo:")
    print("1 - INCLUIR")
    print("2 - REMOVER")
    print("3 - ALTERAR")
    print("4 - LISTAR")
    print("5 - SAIR")
    return int(input("Digite a opção: "))


while True:
    try:
        opcao = menu()

        if opcao == 1:
            item = input("Digite o item para incluir: ")
            dados.append(item)
            print("Item adicionado com sucesso!")

        elif opcao == 2:
            item = input("Digite o item para remover: ")
            if item in dados:
                dados.remove(item)
                print("Item removido!")
            else:
                print("Item não encontrado.")

        elif opcao == 3:
            item = input("Qual item deseja alterar? ")
            if item in dados:
                novo = input("Digite o novo valor: ")
                index = dados.index(item)
                dados[index] = novo
                print("Item alterado com sucesso!")
            else:
                print("Item não encontrado.")

        elif opcao == 4:
            print("\nLista de itens:")
            for i, item in enumerate(dados, start=1):
                print(f"{i} - {item}")

        elif opcao == 5:
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

    except ValueError:
        print("Você digitou um valor inválido! Digite apenas números.")
    
    finally:
        print("Operação finalizada.\n")
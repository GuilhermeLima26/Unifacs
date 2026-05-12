# LISTAS PARA ARMAZENAR OS DADOS
selecoes = []
jogadores = []
estadios = []

def menu():
    while True:
        try:
            print("\n--- MENU PRINCIPAL ---")
            print("1 - INCLUIR")
            print("2 - ALTERAR")
            print("3 - REMOVER")
            print("4 - LISTAR")
            print("5 - SAIR")

            opcao = int(input("Escolha: "))

            if 1 <= opcao <= 5:
                return opcao
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite apenas números!")


def incluir():
    while True:
        print("\n--- INCLUIR ---")
        print("1 - Seleção")
        print("2 - Jogador")
        print("3 - Estádio")
        print("4 - Voltar")

        try:
            opcao = int(input("Escolha: "))

            if opcao == 1:
                nome = input("Nome da seleção: ")
                selecoes.append(nome)
                print("Seleção incluída!")

            elif opcao == 2:
                nome = input("Nome do jogador: ")
                jogadores.append(nome)
                print("Jogador incluído!")

            elif opcao == 3:
                nome = input("Nome do estádio: ")
                estadios.append(nome)
                print("Estádio incluído!")

            elif opcao == 4:
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Erro: digite um número!")


def listar():
    print("\n--- LISTAGEM ---")

    print("\nSeleções:")
    for i, s in enumerate(selecoes):
        print(f"{i} - {s}")

    print("\nJogadores:")
    for i, j in enumerate(jogadores):
        print(f"{i} - {j}")

    print("\nEstádios:")
    for i, e in enumerate(estadios):
        print(f"{i} - {e}")


def remover():
    listar()
    try:
        tipo = int(input("\nRemover de qual lista? (1-Seleção, 2-Jogador, 3-Estádio): "))
        indice = int(input("Digite o índice: "))

        if tipo == 1:
            print(f"Removido: {selecoes.pop(indice)}")
        elif tipo == 2:
            print(f"Removido: {jogadores.pop(indice)}")
        elif tipo == 3:
            print(f"Removido: {estadios.pop(indice)}")
        else:
            print("Tipo inválido!")

    except (ValueError, IndexError):
        print("Erro ao remover!")


def alterar():
    listar()
    try:
        tipo = int(input("\nAlterar qual lista? (1-Seleção, 2-Jogador, 3-Estádio): "))
        indice = int(input("Digite o índice: "))
        novo = input("Novo valor: ")

        if tipo == 1:
            selecoes[indice] = novo
        elif tipo == 2:
            jogadores[indice] = novo
        elif tipo == 3:
            estadios[indice] = novo
        else:
            print("Tipo inválido!")
            return

        print("Alterado com sucesso!")

    except (ValueError, IndexError):
        print("Erro ao alterar!")


# LOOP PRINCIPAL
while True:
    escolha = menu()

    if escolha == 1:
        incluir()
    elif escolha == 2:
        alterar()
    elif escolha == 3:
        remover()
    elif escolha == 4:
        listar()
    elif escolha == 5:
        print("Saindo do sistema...")
        break 
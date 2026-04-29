opcao = 0 
def menu():
    print("Escolha uma das opções abaixo:")
    print("1 - INCLUIR")
    print("2 - REMOVER")
    print("3 - ALTERAR")
    print("4 - LISTAR")
    print("5 - SAIR")
    opcao = int(input())
    if (opcao > 0 and opcao < 5):
        return opcao
    else:
        if (opcao == 5):
            exit(0) #função para sair do sistema

# FAZENDO TRATAMENTO DE EXCESSAÕ
try:
     opcao = menu()

except ValueError:
    print("voce digitou um caracter errado")

except ZeroDivisionError:
    print("nao e possivel dividir por zero.")

else:
    print("codigo executado sem erros.")

finally: 
    print("fim do programa")
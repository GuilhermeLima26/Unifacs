# 1. Mostrar:
# 1
# 2 2
# 3 3 3

def linhas(n):

    for i in range(1, n + 1):

        for j in range(i):
            print(i, end=" ")

        print()


n = int(input("Digite um número: "))
linhas(n)
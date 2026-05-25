# 2. Mostrar:
# 1
# 1 2
# 1 2 3

def numeros(n):

    for i in range(1, n + 1):

        for j in range(1, i + 1):
            print(j, end=" ")

        print()


n = int(input("Digite um número: "))
numeros(n)
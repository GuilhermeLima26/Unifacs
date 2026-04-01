matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input("Digite um número: "))
        linha.append(num)
    matriz.append(linha)

soma = 0

for i in range(3):
    soma += matriz[i][i]

print("Soma:", soma)
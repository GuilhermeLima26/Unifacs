matriz = []

# Ler os valores da matriz
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

# Somar diagonal principal
soma = 0
for i in range(3):
    soma += matriz[i][i]

print("Soma da diagonal principal:", soma)
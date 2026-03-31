num = int(input("Digite um número: "))

contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print("É primo")
else:
    print("Não é primo")
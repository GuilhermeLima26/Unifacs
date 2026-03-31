lista = []

# Pedir 5 números
for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

# Ordenar a lista
lista.sort()

# Mostrar resultado
print("Lista em ordem crescente:", lista)
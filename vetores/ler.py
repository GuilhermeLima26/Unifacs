palavra = input("Digite uma palavra: ")

invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]

print("Palavra invertida:", invertida)
n1 = float(input("digite seu primeiro número:"))
n2 = float(input("digite seu segundo número:"))
n3 = float(input("digite seu terceiro número: "))

if n1>= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else: 
    maior = n3


if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else: 
    menor = n3

print("o maior numero é:", maior)
print("o menor numero é:", menor)

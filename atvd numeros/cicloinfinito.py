soma = 0
quantidade = 0

while True:
    num = int(input("Digite um número (0 para parar): "))
    
    if num == 0:
        break  # sai do loop
    
    soma = soma + num
    quantidade = quantidade + 1

print("Soma:", soma)
print("Quantidade de números:", quantidade)
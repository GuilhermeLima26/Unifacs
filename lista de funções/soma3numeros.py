def soma_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

# Entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chamando a função
resultado = soma_tres_numeros(num1, num2, num3)

# Exibindo o resultado
print("A soma dos três números é:", resultado)
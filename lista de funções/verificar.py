def verificar_numero(numero):
    if numero > 0:
        return "P"
    else:
        return "N"

# Entrada do número
valor = float(input("Digite um número: "))

# Chamando a função
resultado = verificar_numero(valor)

# Mostrando o resultado
print("Resultado:", resultado)
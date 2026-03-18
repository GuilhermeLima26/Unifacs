n1 = float(input("digite seu primeiro número para operação:"))
n2 = float(input("digite seu segundo número para operação:"))
operacao = input("digite a operação (+, -, *, /):")

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

if (operacao == "+"):
    print("a soma dos números é: ", soma)
elif (operacao == "-"):
    print("a subtração dos números é: ", subtracao)
elif (operacao == "*"):
    print("a multiplição dos números é: ", multiplicacao)
elif (operacao == "/"):
    if (n1 == 0  or n2 == 0):
        print("não é possivel divisão por 0")
    else:
        print("a divisão dos números é: ", divisao)
else:
    print("Não foi possivel concluir a operação!")
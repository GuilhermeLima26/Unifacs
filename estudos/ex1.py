n1 = float(input("digite nota 1: "))
n2 = float(input("digite nota 2: "))

media = (n1+n2) /2
mensagem = "BOLETIM ESCOLAR"

if media >= 7:
    print("aluno aprovado, media:", media)
    print(mensagem)
elif media <= 4:
    print("aluno reprovado")
else:
    print("aluno sujeito a recuperação")
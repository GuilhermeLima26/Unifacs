import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Adivinhe o numero entre 1 e 100!")

while True:
    palpite = int(input("seu palpite"))
    tentativas += 1 

    if palpite < numero_secreto:
        print("tente um numero maior.")
    elif palpite > numero_secreto:
        print("tente um numero menor.")
    else:
     print(f"Acertou em {tentativas} tentativas!")
     break
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    # Cálculo do delta
    delta = b**2 - 4*a*c
    print("Delta =", delta)

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print("Uma raiz real:", x)
    else:
        import math
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)

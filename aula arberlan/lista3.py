while True:
    nota = float(input("informe uma nota entre zero e dez"))
    if (nota >= 0 and nota <= 10):
        print(f"voce digitou a nota: {nota:.2}")
        print("e uma nota valida")
        break
    else: 
        print("e uma nota invalida. tente novamente.")
        
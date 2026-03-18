diadasemana = int(input("digite um numero representante o dia da semana: "))

match diadasemana:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")   
    case 4:
        print("quarta")   
    case 5:
        print("quinta")
    case 6:
        print("sexta")   
    case _: 
        print("dia da semana invalido")          
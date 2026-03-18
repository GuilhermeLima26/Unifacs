letra = (input("digite uma letra: ")).lower()

if (letra in ["a","e","i","o","u"]):
    print("e uma volgal")
elif(letra in["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","w","y","z"]):
    print("e uma consoante!")
else:
    print("não e uma letra!")  
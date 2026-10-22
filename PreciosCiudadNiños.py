i = 0
lista= [
[],
[]
]



while i <= 1:
    print("Institucion exonerada?")
    dec = input()
    if dec == "Si" or dec == "si" or dec == "s":
        print("Gratis")
     
    elif dec == "Cerrar":
        break
        
    elif dec == "No" or dec == "no" or dec == "n":
        print("Adultos?")
        adulto = int(input())
        print("Niños?")
        niño = int(input())
        
        lista[0].append(adulto)
        lista[1].append(niño)
    
        print("Cancelan " + str((adulto +(niño * 0.5))))
    print("Fin")
    i += 1

print("Total A: " + str(sum(lista[0])))
print("Total N: " + str(sum(lista[1])))

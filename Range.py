# Range 
numeros = list(range(10)) #Crea una lista con 10 numero, iniciando desde el 0. Llega a 9 en este caso.

print(numeros)

numbers = list(range(3, 8)) #Crea numeros entre el 3 y el 8, iniciando desde el 3 y terminando antes del 8
print(numbers)

abj = list(range(5, 8))
print(len(abj)) # Dice cuantos numeros hay del 5 al 8

pasos = list(range(0, 20, 2)) # El tercer argumento hace que la lista se cree con "pasos" de por medio, Ej. 0, 2, 4, 6...

print(pasos)

for i in range(5):
    print("Bucle for usando range. 5 veces")
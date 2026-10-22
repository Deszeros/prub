inv = [
["Leche", "Agua", "Jugo"],
["Arroz", "Caraota", "Rissotto"],
["Carne", "Pollo", "Cochino"],
["Perro", "Perro", "Perro"]
]

inv[0].append("Manuel") #Append añade el valor al final de la lista señalada en [0]

inv[0].remove("Jugo") #Remove quita el valor señalado, de la lista dicha en [0]


print(len(inv[1])) #Len(x[0]) devuelve la cantidad de valores en una lista como numero. 3 En este caso.

inv[2].insert(1, "Papalo") #Añade valor al lugar elegido de la lista, moviendo los que estaban alli hacia la derecha

inv[0][0] = "a" #Reescribe el valor de la lista señado. Leche por a#

print(inv)

print(inv[3].count("Perro")) #Devuelve la cantidad de veces que se repite un vañor en una lista. En este caso 3 veces




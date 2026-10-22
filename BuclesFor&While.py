#Bucles While

x = 1

while x <= 5:
    print(x)
    x += 1

print("Lito") #Bucle while basico, se establecen los requisitos y lo que se ejecuta dentro.

x = 1
while x <= 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 # Bucle While con un if adentro que muestra los numeros pares y no pares
    
a = 0
while a >= 0:
    print(a)
    a += 1
    if a >= 20:
        print("Break")
        break #Break provoca que el bucle acabe de golpe.

i = 1
while i<=5:
  print(i)
  i+=1
  if i==3:
    print("Skipping 3")
    continue #Continue detiene la repeticion actual y la reinicia desde un principio.
    
#Bucles for

words = ["Papa", "Random", "Loco", "Lele"]

for word in words:
    print(word + "!") #Por cada palabra("Word") en la lista, añade el simbolo ! al final
    
gt = "tetrapoliedro"
count = 0

for ñ in gt:
    if ñ == "t":
        count += 1
        
    print(count)
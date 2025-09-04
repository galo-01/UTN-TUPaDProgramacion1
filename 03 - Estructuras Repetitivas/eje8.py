
#[ ejercicio 8 ]

pares=0
inpares=0
negativos=0
positivos=0

for i in range(0,100,1):
    num = int(input("[Ingrese numero entero]:"))

    if (num%2==0):
        pares +=1
    else:
        inpares +=1
    
    if(num>0):
        positivos+=1
    else:
        negativos+=1


print(f"Pares: {pares}")
print(f"Inpares: {inpares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")        
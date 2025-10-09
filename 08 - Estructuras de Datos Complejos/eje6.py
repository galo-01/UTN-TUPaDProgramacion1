
alumnos = {}


for i in range(3):
    print("")
    alumno = input("[Ingrese del primer alumno]:")
    notas = []
    for i in range(3):
        nota = int(input(f"[Ingrese la nota {i+1} de {alumno}]:"))
        notas.append(nota)
    notas = tuple(notas)
    alumnos[alumno] = notas


print("")
for clave in alumnos:
    print(f"- El promedio de {clave} es de {(alumnos[clave][0]+alumnos[clave][1]+alumnos[clave][2])/3}")


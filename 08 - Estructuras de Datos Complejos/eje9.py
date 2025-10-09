

agenda = {
    ("lunes", "9:00"): "Reunión diaria",
    ("lunes", "14:30"): "Llamada con cliente",
    ("martes", "18"): "Gimnasio",
}


def agendar(dia, hora, evento):
    clave = (dia, hora)
    agenda[clave] = evento.strip()


def consultar(dia, hora):
    print((dia, hora))
    if((dia, hora) in agenda):
        return agenda[(dia, hora)]
    else:
        print("No hay actividad programada para ese dia y hora.")



dia = input("[Ingrese día a consultar (ej. Lunes) ]: ").strip().lower()
hora = input("[IngresehHora a consultar (ej. 09:00 o 14:30) ]: ")

evento = consultar(dia, hora)

if evento:
    print(f"En {dia} a las {hora}: {evento}")
total=int(input("Cuantas preguntas hay en el examen?"))
correcta=int(input("cuantas contestaste correctamente?"))


multi=correcta/total
porcentaje=multi*100

if porcentaje>90:
    print("Tienes el nivel máximo")
else:
    if porcentaje>=75:
        if porcentaje<90:
            print("Tienes el nivel medio")
    else:
        if porcentaje >=50:
            if porcentaje<75:
                print("Tienes un nivel regular")
        else:
            if porcentaje<50:
                print("Fuera de nivel")


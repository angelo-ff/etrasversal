import funciones as fun

while True:
    try:
        fun.limpiar_pantalla()
        fun.titulo("\tVENTAS DE ENTRADAS \n     concierto VIP de “Michael Jam”")
        print("1) Comprar entrada")
        print("2) Mostrar ubicaciones disponibles")
        print("3) Ver listado de asistentes")
        print("4) Mostrar ganancias totales")
        print("0) salir")
        opcion = int(input("Seleccione : "))

        if opcion == 0:
            print("ADIOS")  
            break
        elif opcion >=1 and opcion <= 4:
            fun.printv("Opcion valida")
            if opcion == 1:
                fun.titulo("\t  COMPRA DE ENTRADAS")
                rut = int(input("Ingrese rut sin puntos, guion, ni dígito verificador \nEJ(00000000) : "))
                cant = int(input("Ingrese la cantidad de entradas que desea comprar : "))
                fun.verescenario()
                column = input("Ingrese la columna que desea : ").upper()
                fila = int(input("Ingrese la fila : "))
                fun.comprarentrada(column, fila, rut, cant)
            elif opcion == 2:
                fun.verescenario()
                fun.printa("ASIENTOS DISPONIBLES = 🟩")
                fun.printa("ASIENTOS NO DISPONIBLES = 🟥")
            elif opcion == 3:
                pass
            elif opcion == 4:
                fun.titulo("Ganancias totales")
                fun.ganancias()
        else:
            fun.printr("Opcion no valida")
    except:
        fun.printr("Error en el sistema")
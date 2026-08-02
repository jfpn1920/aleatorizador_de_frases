import random
ids = []
titulos = []
autores = []
categorias = []
frases = []
fechas = []
observaciones = []
#--------------------------------------------#
#--|menu_principal_aleatorizador_de_frases|--#
#--------------------------------------------#
while True:
    print("menu principal aleatorizador de frases")
    print("1) crear frase")
    print("2) editar frase")
    print("3) eliminar frase")
    print("4) buscar frase")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_frase|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_frase = 1
        else:
            id_frase = ids[-1] + 1
        titulo = input("título de la frase: ")
        autor = input("autor: ")
        categoria = input("categoría: ")
        frase = input("frase: ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        ids.append(id_frase)
        titulos.append(titulo)
        autores.append(autor)
        categorias.append(categoria)
        frases.append(frase)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("frase registrada correctamente.")
        print("id:", id_frase)
    #------------------#
    #--|editar_frase|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar frase")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {autores[i]} | {categorias[i]} | {frases[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {autores[posicion]} | {categorias[posicion]} | {frases[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                autores[posicion] = input("nuevo autor: ")
                categorias[posicion] = input("nueva categoría: ")
                frases[posicion] = input("nueva frase: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_frase|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar frase")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {autores[i]} | {categorias[i]} | {frases[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {autores[posicion]} | {categorias[posicion]} | {frases[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    autores.pop(posicion)
                    categorias.pop(posicion)
                    frases.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_frase|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar frase")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {autores[posicion]} | {categorias[posicion]} | {frases[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {autores[i]} | {categorias[i]} | {frases[i]} | {fechas[i]} | {observaciones[i]}")
            print("estadísticas aleatorizador de frases")
            print("cantidad de frases:", len(ids))
            print("autores registrados:", len(autores))
            print("primera frase registrada:", titulos[0])
            print("última frase registrada:", titulos[-1])
            posicion = random.randint(0, len(ids) - 1)
            print("frase seleccionada aleatoriamente")
            print(f"{ids[posicion]} | {titulos[posicion]} | {autores[posicion]} | {categorias[posicion]} | {frases[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de frases.")
        break
    else:
        print("opción no válida.")
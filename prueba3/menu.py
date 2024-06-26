import json
import funciones as fn
import os
import time
while True:
    seleccion = int(input("***************************\n*       MUNDO LIBRO       *\n***************************\n[1] - Mantenedor de categorias\n[2] - Reportes\n[3] - Salir"))

    if seleccion == 1:
        while True:
            seleccionMante = int(input("***************************\n*  MANTENEDOR CATEGORIAS  *\n***************************\n[1] - Agregar categoria\n[2] - Editar categoria\n[3] - Eliminar categoria\n[4] - Buscar categoria\n[5] - Salir"))
            if seleccionMante == 1:

                # AGREGAR CATEGORIA
                nombre = input("Ingrese el nombre de la categoria a agregar")
                fn.agregarCategoria(nombre)

            if seleccionMante == 2:

                # EDITAR CATEGORIA
                parId = int(input("Ingrese el id de la categoria a modificar"))
                nombre = input("Ingrese el nombre que le desea poner a la categoria")
                fn.editarCategoria(parId,nombre)
            if seleccionMante == 3:

                # ELIMINAR CATEGORIA
                parId = int(input("Ingrese el id de la categoria a eliminar"))
                fn.eliminarCliente(parId)
            if seleccionMante == 4:

                # LISTAR CATEGORIAS

                print("************ CATEGORIAS ************")

                with open("biblioteca.json", mode="r") as lecturaJson:
                    archivoJson = json.load(lecturaJson)
                    
                    for i in archivoJson["Categoria"]:
                        print("id: ",i["CategoriaID"], "      ", "Categoria: ",i["Nombre"])
                            
                        
            if seleccionMante == 5:
                print("...")
                break
    if seleccion == 2:
        fn.listarLibros()
        os.system("cls")
        time.sleep(0.5)
        print("Reporte de biblioteca creado exitosamente")

        fn.printReporte()
    if seleccion == 3:
        time.sleep(0.3)
        print("Hasta luego")
        break



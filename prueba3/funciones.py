import json

with open("biblioteca.json", mode = "r") as reporteLectura:
    archivoJson = json.load(reporteLectura)
    contadorLibro_1 = 0
    contadorLibro_2 = 0
    contadorLibro_3 = 0
    contadorLibro_4 = 0
    contadorLibro_5 = 0
    contadorLibro_6 = 0
    contadorLibro_7 = 0
    contadorLibro_8 = 0
    contadorLibro_9 = 0
    contadorLibro_10 = 0
    contadorLibro_11 = 0
    contadorLibro_12 = 0
    contadorLibro_13 = 0
    contadorLibro_14 = 0
    contadorLibro_15 = 0
    contadorLibro_16 = 0
    contadorLibro_17 = 0
    contadorLibro_18 = 0
    contadorLibro_19 = 0
    contadorLibro_20 = 0
    for i in archivoJson["Prestamo"]:
        if i["LibroID"] == 1:
            contadorLibro_1 += 1
        if i["LibroID"] == 2:
            contadorLibro_2 += 1
        if i["LibroID"] == 3:
            contadorLibro_3 += 1
        if i["LibroID"] == 4:
            contadorLibro_4 += 1
        if i["LibroID"] == 5:
            contadorLibro_5 += 1
        if i["LibroID"] == 6:
            contadorLibro_6 += 1
        if i["LibroID"] == 7:
            contadorLibro_7 += 1
        if i["LibroID"] == 8:
            contadorLibro_8 += 1
        if i["LibroID"] == 9:
            contadorLibro_9 += 1
        if i["LibroID"] == 10:
            contadorLibro_10 += 1
        if i["LibroID"] == 11:
            contadorLibro_11 += 1
        if i["LibroID"] == 12:
            contadorLibro_12 += 1
        if i["LibroID"] == 13:
            contadorLibro_13 += 1
        if i["LibroID"] == 14:
            contadorLibro_14 += 1
        if i["LibroID"] == 15:
            contadorLibro_15 += 1
        if i["LibroID"] == 16:
            contadorLibro_16 += 1
        if i["LibroID"] == 17:
            contadorLibro_17 += 1
        if i["LibroID"] == 18:
            contadorLibro_18 += 1
        if i["LibroID"] == 19:
            contadorLibro_19 += 1
        if i["LibroID"] == 20:
            contadorLibro_20 += 1

def agregarCategoria(parNombre:str):
    with open("biblioteca.json", mode = "r") as lecturaCategoria:
        archivoJson = json.load(lecturaCategoria)

    nuevaCategoria = {
        "CategoriaID": len(archivoJson["Categoria"])+1,
        "Nombre": parNombre
    }

    archivoJson["Categoria"].append(nuevaCategoria)

    with open("biblioteca.json", mode = "w") as escrituraJson:
        json.dump(archivoJson,escrituraJson,indent=4)

def editarCategoria(parId:int,parNombre:str):
    with open("biblioteca.json", mode = "r") as lecturaCategoria:
        archivoJson = json.load(lecturaCategoria)
    contador = 0
    for i in archivoJson["Categoria"]:
    
        if i["CategoriaID"] == parId:
            break
        contador += 1

    
    archivoJson["Categoria"][contador]["Nombre"] = parNombre

    with open("biblioteca.json", mode = "w") as escrituraJson:
        json.dump(archivoJson,escrituraJson,indent = 4)

def eliminarCliente(parId):
    with open("biblioteca.json", mode="r") as lecturaCategoria:
        archivoJson = json.load(lecturaCategoria)
        contador = 0
        for i in archivoJson["Categoria"]:
            if i["CategoriaID"] == parId:
                del archivoJson["Categoria"][contador]
                break
            contador += 1

    with open("biblioteca.json", mode = "w") as escrituraJson:
        escrituraJson.truncate()
        json.dump(archivoJson,escrituraJson,indent=4)

def listarLibros():
    with open("biblioteca.json", mode = "r") as reporteLectura:
            archivoJson = json.load(reporteLectura)
            
            reporte = {
                archivoJson["Libro"][0]["Titulo"]: contadorLibro_1,
                archivoJson["Libro"][1]["Titulo"]: contadorLibro_2,
                archivoJson["Libro"][2]["Titulo"]: contadorLibro_3,
                archivoJson["Libro"][3]["Titulo"]: contadorLibro_4,
                archivoJson["Libro"][4]["Titulo"]: contadorLibro_5,
                archivoJson["Libro"][5]["Titulo"]: contadorLibro_6,
                archivoJson["Libro"][6]["Titulo"]: contadorLibro_7,
                archivoJson["Libro"][7]["Titulo"]: contadorLibro_8,
                archivoJson["Libro"][8]["Titulo"]: contadorLibro_9,
                archivoJson["Libro"][9]["Titulo"]: contadorLibro_10,
                archivoJson["Libro"][10]["Titulo"]: contadorLibro_11,
                archivoJson["Libro"][11]["Titulo"]: contadorLibro_12,
                archivoJson["Libro"][12]["Titulo"]: contadorLibro_13,
                archivoJson["Libro"][13]["Titulo"]: contadorLibro_14,
                archivoJson["Libro"][14]["Titulo"]: contadorLibro_15,
                archivoJson["Libro"][15]["Titulo"]: contadorLibro_16,
                archivoJson["Libro"][16]["Titulo"]: contadorLibro_17,
                archivoJson["Libro"][17]["Titulo"]: contadorLibro_18,
                archivoJson["Libro"][18]["Titulo"]: contadorLibro_19,
                archivoJson["Libro"][19]["Titulo"]: contadorLibro_20
            }
    with open("Reportes_biblioteca_mundo_libro.json", mode = "w") as escrituraJson:
        json.dump(reporte,escrituraJson, indent=4)
def printReporte():
    with open("biblioteca.json", mode = "r") as reporteLectura:
            archivoJson = json.load(reporteLectura)
           
    print(f"""********************************************************************************
* LIBROS                                            CANTIDAD DE VECES PRESTADO *
********************************************************************************
{archivoJson["Libro"][0]["Titulo"]}: {contadorLibro_1},
{archivoJson["Libro"][1]["Titulo"]}: {contadorLibro_2},
{archivoJson["Libro"][2]["Titulo"]}: {contadorLibro_3},
{archivoJson["Libro"][3]["Titulo"]}: {contadorLibro_4},
{archivoJson["Libro"][4]["Titulo"]}: {contadorLibro_5},
{archivoJson["Libro"][5]["Titulo"]}: {contadorLibro_6},
{archivoJson["Libro"][6]["Titulo"]}: {contadorLibro_7},
{archivoJson["Libro"][7]["Titulo"]}: {contadorLibro_8},
{archivoJson["Libro"][8]["Titulo"]}: {contadorLibro_9},
{archivoJson["Libro"][9]["Titulo"]}: {contadorLibro_10},
{archivoJson["Libro"][10]["Titulo"]}: {contadorLibro_11},
{archivoJson["Libro"][11]["Titulo"]}: {contadorLibro_12},
{archivoJson["Libro"][12]["Titulo"]}: {contadorLibro_13},
{archivoJson["Libro"][13]["Titulo"]}: {contadorLibro_14},
{archivoJson["Libro"][14]["Titulo"]}: {contadorLibro_15},
{archivoJson["Libro"][15]["Titulo"]}: {contadorLibro_16},
{archivoJson["Libro"][16]["Titulo"]}: {contadorLibro_17},
{archivoJson["Libro"][17]["Titulo"]}: {contadorLibro_18},
{archivoJson["Libro"][18]["Titulo"]}: {contadorLibro_19},
{archivoJson["Libro"][19]["Titulo"]}: {contadorLibro_20}
""")
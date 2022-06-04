import operator

def main(lista_texto):
    lista = lista_texto.split(' ') #Creamos una lista que contiene cada una de las palabras
    #print(lista)
    diccionario = {}
    for palabra in lista: #Creamos un ciclo para que contabilice las veces que se repite la palabra
        times = 0
        for i in lista:
            if i == palabra:
                times += 1
                    # if times >1:

        #print(f"la palabra {palabra} aparece {times} veces")
        diccionario[palabra] = [times]  #Creamos un diccionario que almacena la palabra y la cantidad de veces que se repite esa palabra.
    #print(diccionario)

    diccionariosort = sorted(diccionario.items(), key=operator.itemgetter(1),reverse= True) #Importamos el método operator y ordenamos los valores del diccionario de mayor a menor
    #print("diccionario sorted") #El problema es que me crea una lista de tuplas, necesito una lista de listas.
    #print(diccionariosort)

    nuevodiccionario = {} #Creamos un nuevo diccionario

    for k, v in diccionariosort:  #Agregamos las llaves y los valores ordenados en el código anterior
        nuevodiccionario[k] = v
    #print(nuevodiccionario)

    listaTimes = nuevodiccionario.values()
    listaPalabra = nuevodiccionario.keys()
    listaPalabra = list(listaPalabra)
    #print(listaPalabra)
    listaTimes = list(listaTimes)
    listaRetorno = []

    for i in range(len(nuevodiccionario)): #Por medio de este ciclo creamos la lista de listas
        listaTotal = [listaPalabra[i], listaTimes[i]]
        listaRetorno.append(listaTotal)
    #print(listaRetorno)

    listaMayores = []
    i = 0
    for times in listaRetorno:
        if i < 20:
            listaMayores.append(times)
            i += 1
    print(listaMayores)








    '''
    listaTimes = diccionario.values()
    listaPalabra = diccionario.keys()
    listaPalabra = list(listaPalabra)
    print(listaPalabra)
    listaTimes = list(listaTimes)

    listaTotal = []
    listaRetorno = []
    for i in range(len(listaTimes)):
        listaTotal = [listaPalabra[i], listaTimes[i]]
        #print(listaTotal)
        listaRetorno.append(listaTotal)
    #print(listaRetorno)
    #listaRetorno.sort(reverse=True)
    listaTimes.sort(reverse =True)
    print(listaRetorno)
    #print(listaTimes)
    listaMayores = []
    i = 0
    for times in listaTimes:
        if i < 20:
            listaMayores.append(times)
            i += 1
    print(listaMayores)


    listaFinal= []
    
    '''



texto = ("""Usted forma parte de un equipo que se dedica a analizar textos pequeños para conocer su composición. Los compañeros de equipo han creado a partir de un cuento breve una lista de Python que contiene cada una de las palabras que lo componen; pero en la creación de la lista de palabras no evitaron que aparecieran adheridos a algunas de las palabras los signos de puntuación ni los guiones que estaban dentro del cuento original. A pesar de ello, a usted le han delegado determinar cuáles son las 20 palabras más frecuentes en esta lista de Python y también la cantidad de veces que cada una de ellas aparece en la lista, con las siguientes condiciones: Cada una de las 20 palabras más frecuentes y su conteo de veces deben estar juntas en una lista así: (palabra, conteo_de_veces).""")
main(texto)

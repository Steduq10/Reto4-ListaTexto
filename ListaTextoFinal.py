import operator
def main(lista_texto):
    lista_texto = lista_texto.split(' ')  # Creamos una lista que contiene cada una de las palabras
    for i in range(len(lista_texto)): #Convertimos el contenido de la lista en minúscula
        lista_texto[i] = lista_texto[i].lower()

    caracteres = ['-','¿','?','.',',','¡','!',':','"','–']
    for j in range(len(lista_texto)):   #Necesitamos remover los signos de puntuación
        for i in range(len(caracteres)):
            lista_texto[j] = lista_texto[j].replace(caracteres[i],"")

    for i in range(len(lista_texto)-1, -1, -1):
        if not lista_texto[i]:
            del lista_texto[i]
    print(lista_texto)


    #lista = lista_texto
    #print(lista)
    diccionario = {}
    for palabra in lista_texto:  # Creamos un ciclo para que contabilice las veces que se repite la palabra
        times = 0
        for i in lista_texto:
            if i == palabra:
                times += 1
        #print(times)
        diccionario[palabra] = times  # Creamos un diccionario que almacena la palabra y la cantidad de veces que se repite esa palabra.
    #print(diccionario)

    diccionariosort = sorted(diccionario.items(), key=operator.itemgetter(1),
                             reverse=True)  # Importamos el método operator y ordenamos los valores del diccionario de mayor a menor
     #El problema es que me crea una lista de tuplas, necesito una lista de listas.


    nuevodiccionario = {}  # Creamos un nuevo diccionario

    for k, v in diccionariosort:  # Agregamos las llaves y los valores ordenados en el código anterior
        nuevodiccionario[k] = v

    listaTimes = nuevodiccionario.values()
    listaPalabra = nuevodiccionario.keys()
    listaPalabra = list(listaPalabra)
    listaTimes = list(listaTimes)
    listaRetorno = []

    for i in range(len(nuevodiccionario)):  # Por medio de este ciclo creamos la lista de listas
        listaTotal = [listaPalabra[i], listaTimes[i]]
        listaRetorno.append(listaTotal)



    lista_conteo = []
    i = 0
    for times in listaRetorno:
        if i < 20:
            lista_conteo.append(times)
            i += 1
    print(lista_conteo)
    return lista_conteo
textos = (
    """Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. Python es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites. Con el paso del tiempo, Python ha ido ganando adeptos gracias a su sencillez y a sus amplias posibilidades, sobre todo en los últimos años, ya que facilita trabajar con inteligencia artificial, big data, machine learning y data science, entre muchos otros campos en auge.  """)
main(textos)
"""Usted forma parte de un equipo que se dedica a analizar textos pequeños para conocer su composición. Los compañeros de equipo han creado a partir de un cuento breve una lista de Python que contiene cada una de las palabras que lo componen; pero en la creación de la lista de palabras no evitaron que aparecieran adheridos a algunas de las palabras los signos de puntuación ni los guiones que estaban dentro del cuento original. A pesar de ello, a usted le han delegado determinar cuáles son las 20 palabras más frecuentes en esta lista de Python y también la cantidad de veces que cada una de ellas aparece en la lista, con las siguientes condiciones: Cada una de las 20 palabras más frecuentes y su conteo de veces deben estar juntas en una lista así: (palabra, conteo_de_veces)."""
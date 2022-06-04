import operator
from collections import Counter
def main(lista_texto):
    lista_texto = lista_texto.split()
    for i in range(len(lista_texto)):
        lista_texto[i] = lista_texto[i].lower()
    caracteres = ['-', '¿', '?', '.', ',', '¡', '!', ':', '"', '–']
    for j in range(len(lista_texto)):  # Necesitamos remover los signos de puntuación
        for i in range(len(caracteres)):
            lista_texto[j] = lista_texto[j].replace(caracteres[i], "")

    for i in range(len(lista_texto) - 1, -1, -1):
        if not lista_texto[i]:
            del lista_texto[i]
    #print(lista)
    c =Counter(lista_texto)
    #print(c)

    #print(c.most_common(20))

    nuevodiccionario = {}  # Creamos un nuevo diccionario

    for k, v in c.most_common(20):  # Agregamos las llaves y los valores ordenados en el código anterior
        nuevodiccionario[k] = v

    #print(nuevodiccionario)

    listaTimes = nuevodiccionario.values()
    listaPalabra = nuevodiccionario.keys()
    listaPalabra = list(listaPalabra)
    listaTimes = list(listaTimes)
    lista_conteo = []

    for i in range(len(nuevodiccionario)):  # Por medio de este ciclo creamos la lista de listas
        listaTotal = [listaPalabra[i], listaTimes[i]]
        lista_conteo.append(listaTotal)

    print(lista_conteo)
texto = (
    """Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. Python es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites. Con el paso del tiempo, Python ha ido ganando adeptos gracias a su sencillez y a sus amplias posibilidades, sobre todo en los últimos años, ya que facilita trabajar con inteligencia artificial, big data, machine learning y data science, entre muchos otros campos en auge.  """)
main(texto)
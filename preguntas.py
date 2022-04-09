"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv

    total = 0

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for registro in csv_reader:
            total += int(registro[1])

    return total 


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    import csv

    tupla = dict()

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for registro in csv_reader:
            if registro[0] in tupla:
                tupla[registro[0]] += 1
            else:
                tupla[registro[0]] = 1

    listaTuplas = list(tupla.items())
    listaTuplas.sort(key = lambda x: x[0])

    return listaTuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    import csv

    tupla = dict()

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for registro in csv_reader:
            if registro[0] in tupla:
                tupla[registro[0]] += int(registro[1])
            else:
                tupla[registro[0]] = int(registro[1])

    listaTuplas = list(tupla.items())
    listaTuplas.sort(key = lambda x: x[0])

    return listaTuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv

    tupla = dict()

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for registro in csv_reader:
            mes = registro[2].split("-")[1]
                
            if mes in tupla:
                tupla[mes] += 1
            else:
                tupla[mes] = 1

    listaTuplas = list(tupla.items())
    listaTuplas.sort(key = lambda x: x[0])

    return listaTuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    import csv

    tupla = []
    tuplaFinal=[]
    numeroMenor=0
    numeroMayor=0
    letraActual = ''

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
        listaDatos.sort(key = lambda x: (x[0], x[1]))
        
        for registro in listaDatos:
            tupla.append((registro[0],registro[1]))
        
        letraMenorInicial = tupla[0][0]
        numeroMenorInicial = tupla[0][1]

        for x,y in tupla:
            if letraMenorInicial == x:
                if numeroMenorInicial > y:
                    numeroMenor = y
                    numeroMayor = numeroMenorInicial
                    letraActual=x
                else:
                    if numeroMenorInicial < y:
                        numeroMenor = numeroMenorInicial
                        numeroMayor = y
                        letraActual=x
            else:      
                letraMenorInicial = x
                numeroMenorInicial = y
                tuplaFinal.append((letraActual,int(numeroMayor),int(numeroMenor)))

        tuplaFinal.append((letraActual,int(numeroMayor),int(numeroMenor)))
            
    return tuplaFinal


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv

    tupla = ()
    listaDiccionarios = []
    tuplaFinal=[]
    numeroMenor=0
    numeroMayor=0
    letraActual = ''

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
            
        for registro in listaDatos:
            tupla = tupla + (tuple((registro[4].split(','))))

        for registro in tupla:
            listaDiccionarios.append(tuple((registro.split(':'))))
        
        listaDiccionarios.sort(key = lambda x: (x[0], int(x[1])))
        
        letraMenorInicial = listaDiccionarios[0][0]
        numeroMenorInicial = listaDiccionarios[0][1]

        for x,y in listaDiccionarios:
            if letraMenorInicial == x:
                if int(numeroMenorInicial) > int(y):
                    numeroMenor = y
                    numeroMayor = numeroMenorInicial
                    letraActual=x
                else:
                    if int(numeroMenorInicial) < int(y):
                        numeroMenor = numeroMenorInicial
                        numeroMayor = y
                        letraActual=x
            else:      
                letraMenorInicial = x
                numeroMenorInicial = y
                tuplaFinal.append((letraActual,int(numeroMenor),int(numeroMayor)))

        tuplaFinal.append((letraActual,int(numeroMenor),int(numeroMayor)))
    
    return tuplaFinal


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    listaNumeroUnicos = []
    listaParejaLetraNumero = []
    listaLetras = []
    tuplaFinal=[]

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
        
        for registro in listaDatos:
            listaNumeroUnicos.append(((registro[1])))

        listaNumeroUnicos = list(dict.fromkeys(listaNumeroUnicos))
        listaNumeroUnicos.sort(key = lambda x: x[0])

        for registro in listaDatos:
            listaParejaLetraNumero.append(((registro[0],registro[1])))

        for numero in listaNumeroUnicos:
            for pareja in listaParejaLetraNumero:
                if numero == pareja[1]:
                    listaLetras.append(pareja[0])
            
            listaLetrasFinal = listaLetras.copy()
            tuplaFinal.append((int(numero), listaLetrasFinal))
            listaLetras.clear()

    return tuplaFinal


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    import csv

    listaNumeroUnicos = []
    listaParejaLetraNumero = []
    listaLetras = []
    tuplaFinal=[]

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
        
        for registro in listaDatos:
            listaNumeroUnicos.append(((registro[1])))

        listaNumeroUnicos = list(dict.fromkeys(listaNumeroUnicos))
        listaNumeroUnicos.sort(key = lambda x: x[0])

        for registro in listaDatos:
            listaParejaLetraNumero.append(((registro[0],registro[1])))
        
        listaParejaLetraNumero.sort(key = lambda x: x[0])
        listaParejaLetraNumero = list(dict.fromkeys(listaParejaLetraNumero))

        for numero in listaNumeroUnicos:
            for pareja in listaParejaLetraNumero:
                if numero == pareja[1]:
                    listaLetras.append(pareja[0])
            
            listaLetrasFinal = listaLetras.copy()
            tuplaFinal.append((int(numero), listaLetrasFinal))
            listaLetras.clear()

    return tuplaFinal    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    import csv

    tupla = ()
    listaDiccionarios = []
    diccionarioFinal = {}
    claveInicial = ''
    totalVeces = 0

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
            
        for registro in listaDatos:
            tupla = tupla + (tuple((registro[4].split(','))))

        for registro in tupla:
            listaDiccionarios.append(tuple((registro.split(':'))))
        
        listaDiccionarios.sort(key = lambda x: (x[0], int(x[1])))
        
        claveInicial = listaDiccionarios[0][0]
        for registro in listaDiccionarios:
            if claveInicial == registro[0]:
                totalVeces +=1
            else:
                diccionarioFinal[claveInicial] = totalVeces
                claveInicial = registro[0]
                totalVeces=1
            
        diccionarioFinal[claveInicial] = totalVeces

    return diccionarioFinal


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv

    listaElementos = []
    listaElementosFinales = []

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        
        listaDatos = list(csv_reader)
            
        for registro in listaDatos:
            listaElementos.append(tuple((registro[0],registro[3],registro[4])))

        for registro in listaElementos:
            totalSegundosElmentos = len(registro[1].split(','))
            totalTercerosElementos = len(registro[2].split(','))
            listaElementosFinales.append(tuple((registro[0],totalSegundosElmentos,totalTercerosElementos)))
    
    return listaElementosFinales


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

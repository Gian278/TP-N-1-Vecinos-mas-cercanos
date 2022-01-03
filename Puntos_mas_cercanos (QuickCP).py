import csv      #para leer .csv
import time     #para ver cuanto tarda
from math import sqrt       #para calcular las raices
import random   #para la lista de coordenadas aleatorias
#import matplotlib.pyplot as plt     #para graficar



def distancia(dX, dY):      #calcular distancia entre 2 puntos con dX y dY
    return sqrt((dX **2) + (dY **2))

def distancia2(x1,y1,x2,y2):    #lo mismo, pero para distintos formatos de entrada
    return sqrt(((x2-x1) **2) + ((y2-y1) **2))


def formateoRadix(L):

    print("Empezando formateo de la lista...")  #feedback

    n1 = 0      #cantidad de digitos enteros
    n2 = 0      #cantidad de digitos decimales
    LC=[[] for e in range(len(L))]  #lista en la cual voy a cargar todo

    for i in L:     #itera en cada elemento de la lista (pares XY)
        for j in i:     #itera en cada valor de la sublista (X o Y)

            pos1 = 0            #indice del primer digito
            pos2 = len(j) -1    #indice del ultimo digito

            try:
                while j[pos1] != '.':   #continua incrementando hasta detectar "."
                    pos1 +=1

                    if n1 < pos1:   #se asigna a n1 para tener el maximo
                        n1 = pos1
            
            except IndexError:

                if n1 < len(j):   #se asigna a n1 para tener el maximo
                        n1 = len(j)

            try:
                while j[pos2] != '.':   #continua decreciendo hasta detectar "."
                    pos2 -=1

                    if n2 < pos2:   #se asigna a n2 para tener el maximo
                        n2 = pos2

            except IndexError:

                if n2 < len(j):   #se asigna a n1 para tener el maximo
                        n2 = len(j)

    print("Cantidad de digitos enteros:",n1)       #cuantos digitos hay antes del punto
    print("Cantidad de digitos decimales:",n2)       #cuantos digitos hay despues del punto

    conteo = 0
    for i in L:         #itera en cada elemento de la lista (pares XY)
        for j in i:     #itera en cada valor de la sublista (X o Y)

            pos3 = 0    #para saber cuantos digitos enteros tiene el valor actual
            
            try:
                while j[pos3] != '.' :  #iterar hasta alcanzar un punto
                    pos3 +=1

            except IndexError:

                j = j + ".0"        #en caso de no encontrar un punto significa que es un entero
                pos3 = 0            #por lo que agrego el .0 manualmente

                while j[pos3] != '.' :  #vuelvo a buscar el punto agregado
                    pos3 +=1

            if pos3 < n1:   #añadir 0 al principio hasta alcanzar n1
                for o in range(n1-pos3):
                    j = "0" + j

            #ahora j[n1] = punto

            if (len(j) -1) < n1 + n2:   #para saber cuantos decimales enteros tiene el valor actual
                for o in range(n1 + n2 - (len(j) -1)):      #se cuenta al reves
                    j = j + "0" 

            LC[conteo//2].append(j)   #pasaje a la lista nueva
            conteo += 1     #Como son pares XY en una lista plana, paso los 2 a la misma sublista 
                            #Uno despues del otro, truncando el indice actual cuando vale .5

    print("Formateo terminado\n")   #feedback

    return LC   #devuelvo la lista con el formato cambiado



def radixSortLSD(L2,posElemAusar):      #declaro la funcion para ordenar las listas

    print("Ordenando...")   #feedback

    m = len(L2[0][0])   #cantidad de elementos en el primer valor
                        #todos quedaron iguales, por lo que solo mido uno
    LC2 = L2.copy()     #nueva lista en donde cargar valores ordenados

    for i in range(m-1, -1, -1):  #iterar en la lista por posicion de digito, del menos significativo al mas significativo

        if L2[0][0][i] == '.':  #salteo el caso en que se leeria el '.' (se trabaja con strings)
            continue    #prosigo con el proximo caso del for

        G2 = [[] for gp in range(10)]   #lista auxiliar para el ordenamiento
                                        #contiene 10 sulistas vacias, una para cada digito (0-9)

        for j in range(len(L2)):    #iterar en la lista por elemento

            G2[int(LC2[j][int(posElemAusar)][i])].append(LC2[j])    #el mejor y a la vez peor comando del programa
            #en la lista auxiliar (la de 10 sublistas), guardo un elemento dependiendo del digito en
            #la posicion que me interese en este bucle, convirtiendolo a entero y usandolo como indice

        LC2 = []    #vacio la lista para volver a cargarla con el proximo paso

        for j in G2:    #desanido las listas para poder repetir el paso anterior
            LC2 += j

    return LC2  #devuelvo la lista ordenada



def fuerzaBruta(listaX):    #defino la funcion 

    minDist = 100000.0      #asigno un valor muy alto como distancia minima para compararlo con otros
    
    for i in range(len(listaX)-1):  #iterar por cada elemento a excepcion del ultimo

        for j in range(i+1,len(listaX)):    #iterar solo por los elementos posteriores al seleccionado por el for anterior
                                            #para evitar calcular dos veces la misma distancia pero con los puntos al reves
            dist = distancia2(listaX[i][0],listaX[i][1],listaX[j][0],listaX[j][1])   #calculo la distancia con dicha funcion

            if dist < minDist:      #si la distancia medida es menor a la conocida previamente 
                minDist = dist      #actualizar dicha distancia
                respuesta = [listaX[i],listaX[j]]   #y guardar los puntos a los cuales corresponde

    return [respuesta[0],respuesta[1],minDist]      #una vez terminado, devolver los puntos y la distancia



def quickCP(listaX,listaY):     #declaro la funcion (Quick Closest Pair)

    print("Buscando par mas cercano...")    #feedback

    A = listaX.copy()       #copio las listas ordenadas por las dudas
    B = listaY.copy()
    minDist = 100000.0      #inicio con una distancia muy grande entre puntos para compararla

    for ronda in range(1,len(listaX)-1):    #iterar alterando la distancia entre pares en un mismo eje

        print(" Ronda",ronda)   #feedback
        deltaXmin,deltaYmin = 100000.0, 100000.0    #lo mismo que con minDist, pero para distancias que puede que no existan

        for i in range(1,len(listaX)-ronda):    #iterar entre todos los pares a cierta distancia fija (de indices)

            deltaX = A[i+ronda-1][0] - A[i-1][0]    #calcular dX del par actual en la lista ordenada en X
            deltaY = A[i+ronda-1][1] - A[i-1][1]    #calcular dY del par actual en la lista ordenada en X

            if deltaX < deltaXmin:      #modificar la dX ideal del ciclo si es que es menor
                deltaXmin = deltaX

            distA = distancia(deltaX,deltaY)    #calcular la distancia entre el par de puntos de la lista ordenada en X


            deltaX = B[i+ronda-1][0] - B[i-1][0]    #calcular dX del par actual en la lista ordenada en Y
            deltaY = B[i+ronda-1][1] - B[i-1][1]    #calcular dY del par actual en la lista ordenada en Y

            if deltaY < deltaYmin:      #modificar la dY ideal del ciclo si es que es menor
                deltaYmin = deltaY

            distB = distancia(deltaX,deltaY)    #calcular la distancia entre el par de puntos de la lista ordenada en Y


            if distA < minDist and distA < distB:   #actualizar la distancia minima en caso de que lo medido sea menor
                minDist = distA
                punto1 = [A[i+ronda-1][0],A[i+ronda-1][1]]  #guardar los puntos que dieron esa distancia
                punto2 = [A[i-1][0],A[i-1][1]]              #guardar los puntos que dieron esa distancia

            elif distB < minDist and distB < distA:
                minDist = distB
                punto1 = [B[i+ronda-1][0],B[i+ronda-1][1]]  #guardar los puntos que dieron esa distancia
                punto2 = [B[i-1][0],B[i-1][1]]              #guardar los puntos que dieron esa distancia

        if minDist < distancia(deltaXmin, deltaYmin):   #si la distancia ideal del ciclo actual es mayor a la menor
            break                                       #distancia del ciclo antrior, no existe ninguna distancia menor
                                                        #en los posibles pares que quedan, por lo que el programa termina

    return [punto1,punto2,minDist]      #devuelvo los puntos y la distancia entre ellos



def listaRandom(cant):
    return [[str(random.uniform(0,9999.9999)),str(random.uniform(0,9999.9999))] for i in range(cant)]
    #llenar una lista de N elementos con numeros aleatorios
    print("Lista aleatoria creada")     #feedback



def leerCSV(nombreCSV):    #defino la funcion para poder leer los archivos .csv

    listaCSVcoords = []    #Declaro la funcion en la cual voy a cargar el .csv

    with open(str(nombreCSV), 'r') as fileC1:   #leo el archivo
    
        lectorC1 = csv.reader(fileC1)       #copio el contenido en una variable

        for line in lectorC1:           #"lectorC1" es algo llamado <class '_csv.reader'> por lo que
            listaCSVcoords.append(line)    #paso las lineas como sublistas adentro de una sola lista

    return listaCSVcoords   #devuelvo la lista de pares de coordenadas





print("\n Ingrese 1 si desea calcular el par mas cercano en un archivo CSV")
print(" Ingrese 2 si desea calcular el par mas cercano en una lista aleatoria\n")
select = int(input())   #elegir opcion a realizar

if select == 1:

    nombreArchivo = str(input("\nIngrese el nombre del archivo CSV: ")) #se puede usar cualquier archivo
                                                            #que este en la misma ubicacion que este .py

    print("Elija el metodo con el cual procesar los datos:")
    print(" Ingrese 1 para usar Fuerza Bruta")
    print(" Ingrese 2 para usar QuickCP")
    metodo = int(input())       #elegir opcion a realizar

    if metodo == 1:

        aa = time.time()
        strOrdX = radixSortLSD(formateoRadix(leerCSV(nombreArchivo)), 0)    #asigno la lista ordenada en X a otra variable
        bb = time.time() -aa

        print("\n Tiempo de ordenamiento:", bb)

        floatOrdX = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en X

        for i in strOrdX:       #paso los valores (como flotantes)
            floatOrdX.append([float(j) for j in i])

        print("\nIniciando Fuerza Bruta...\n")   #feedback

        aa = time.time()
        Respuesta = fuerzaBruta(floatOrdX)  #llamo a la funcion de Fuerza Bruta y guardo lo que davuelva
        bb = time.time() -aa
        
        print("\n Punto 1:", Respuesta[0], "\n Punto 2:", Respuesta[1], "\n Distancia minima:", Respuesta[2])

        
        print("\n Tiempo de calculo:",bb,"\n")       #imprimo la respuesta y el tiempo que tardo


    if metodo == 2:

        aa = time.time()
        listaFormateada = formateoRadix(leerCSV(nombreArchivo))     #leo el CSV y modifico los valores
                                                            #para que puedan ser ordenados con RadixSort
        strOrdX = radixSortLSD(listaFormateada, 0)    #asigno la lista ordenada en X a otra variable
        strOrdY = radixSortLSD(listaFormateada, 1)    #asigno la lista ordenada en Y a otra variable
        bb = time.time() -aa

        print("\n Tiempo de ordenamiento en X y en Y:", bb)

        floatOrdX = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en X
        floatOrdY = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en Y

        for i in strOrdX:       #paso los valores (como flotantes)
            floatOrdX.append([float(j) for j in i])

        for i in strOrdY:       #paso los valores (como flotantes)
            floatOrdY.append([float(j) for j in i])

        aa = time.time()
        Respuesta = quickCP(floatOrdX,floatOrdY)    #llamo a la funcion y guardo lo que devuelva
        print("\nPunto 1:", Respuesta[0], "\nPunto 2:", Respuesta[1], "\nDistancia minima:", Respuesta[2])
        bb = time.time() -aa
        print("\nTiempo de calculo:",bb,"\n")   #imprimo la respuesta y el tiempo que tardo



elif select == 2:

    print("Ingrese la cantidad de elementos a procesar...")
    cantElem = int(input())     #pido cuantos elementos se quieren usar

    listaAleatoria = listaRandom(cantElem)  #creo la lista aleatoria (valores desde 0 a 9999.9999)

    print("Elija el metodo con el cual procesar los datos:")
    print(" Ingrese 1 para usar Fuerza Bruta")
    print(" Ingrese 2 para usar QuickCP")
    metodo = int(input())   #pregunto el metodo que se quiere usar

    if metodo == 1:

        aa = time.time()
        strOrdX = radixSortLSD(formateoRadix(listaRandom(cantElem)), 0)    #asigno la lista ordenada en X a otra variable
        bb = time.time() -aa

        print("\n Tiempo de ordenamiento:", bb)

        floatOrdX = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en X

        for i in strOrdX:       #paso los valores (como flotantes)
            floatOrdX.append([float(j) for j in i])

        print("\nIniciando Fuerza Bruta...\n")   #feedback
        aa = time.time()

        Respuesta = fuerzaBruta(floatOrdX)
        print("\nPunto 1:", Respuesta[0], "\nPunto 2:", Respuesta[1], "\nDistancia minima:", Respuesta[2])

        bb = time.time() -aa
        print("\nTiempo de calculo:",bb,"\n")   #imprimo la respuesta y el tiempo que tardo


    elif metodo == 2:

        aa = time.time()
        listaFormateada = formateoRadix(listaRandom(cantElem))
        strOrdX = radixSortLSD(listaFormateada, 0)    #asigno la lista ordenada en X a otra variable
        strOrdY = radixSortLSD(listaFormateada, 1)    #asigno la lista ordenada en Y a otra variable
        bb = time.time() -aa

        print("Tiempo de ordenamiento en X y en Y:", bb)

        floatOrdX = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en X
        floatOrdY = []      #creo una lista en la cual cargar los flotantes (actualmente son strings) ordenados en Y

        for i in strOrdX:       #paso los valores (como flotantes)
            floatOrdX.append([float(j) for j in i])

        for i in strOrdY:       #paso los valores (como flotantes)
            floatOrdY.append([float(j) for j in i])

        aa = time.time()
        Respuesta = quickCP(floatOrdX,floatOrdY)
        print("\n Punto 1:", Respuesta[0], "\n Punto 2:", Respuesta[1], "\n Distancia minima:", Respuesta[2])
        bb = time.time() -aa
        print("\n Tiempo de calculo:",bb,"\n")   #imprimo la respuesta y el tiempo que tardo

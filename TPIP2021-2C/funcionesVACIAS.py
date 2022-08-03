from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente
    palabraAzar = random.choice(lista)
    while(len(palabraAzar)<4):
        palabraAzar = random.choice(lista)
    inicioMedio = random.randrange(1,len(palabraAzar)-1)
    finMedio = random.randrange(inicioMedio, len(palabraAzar)-1)
    usados = []

    carga(palabraAzar, usados, listaIzq  , posicionesIzq  , 0             ,inicioMedio     , 0              , ANCHO//3)
    carga(palabraAzar, usados, listaMedio, posicionesMedio, inicioMedio   ,finMedio        , ANCHO//3       , 2* ANCHO//3)
    carga(palabraAzar, usados, listaDer  , posicionesDer  , finMedio      ,len(palabraAzar), 2* ANCHO//3    , ANCHO)


def carga(palabraAzar, usados, lista, posiciones, palDesde, palHasta, xDesde, xHasta):
    for i in range(palDesde, palHasta):
        lista.append(palabraAzar[i])
        x = random.randrange(xDesde+10, xHasta-50)
        while (estaCerca(x, usados)):
            x = random.randrange(xDesde+10, xHasta-50)
        usados.append(x)
        y = 0
        posiciones.append([x,y])


def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    i=0

    while i < len(posiciones):
        y=1
        suma=20
        if posiciones[i][y] < (ALTO-100):
            posiciones[i][y]= posiciones[i][y]+suma
            i= i+1

        else:
            if posiciones[i][y] > ALTO - 101:
                lista.pop(i)
                posiciones.pop(i)

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)

    azar= random.randrange(0,100+1)

    if azar >0 and azar <21:
        cargarListas (lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
     for num in lista:
        if (abs(elem-num)< 10):
            return True
     return False




def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata
    puntaje = 0

    for char in candidata:
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
            puntaje= puntaje+1
        elif char=="j" or char=="k" or char=="q" or char=="w" or char=="x" or char=="y" or char=="z" or char=="h" or char=="ñ":
            puntaje=puntaje+5
        else:
            puntaje=puntaje+2
    return puntaje



def procesar(lista, candidata, listaIzq, listaMedio, listaDer):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    puntaje = 0
    if esValida(lista, candidata, listaIzq, listaMedio, listaDer):
        puntaje = puntaje + Puntos(candidata)
    else:
        if not esValida(lista, candidata, listaIzq, listaMedio, listaDer):
            puntaje = 0

    return (puntaje)

def estaEnLista (lista,elem):
    for elemento in lista:
        if elemento==elem:
            return True

    return False

def interseccion (lista1, lista2):
    for elemento in lista1:
        if estaEnLista(lista2,elemento):
            return True

    return False


def esValida(lista, candidata, listaIzq, listaMedio, listaDer):
    #devuelve True si candidata cumple con los requisitos
    candi=[]
    for elem in candidata:
        candi.append(elem)
    if candidata in lista:
        if interseccion(candi,listaIzq)and interseccion(candi,listaMedio) and interseccion(candi,listaDer):
         return True
    else:
        return False










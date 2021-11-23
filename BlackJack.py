#Importamos cartas

import random
import sys

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

#Convertir diccionario en lista

print(cartas)
listacartas = list(cartas.keys()) * 4
numerodecartas = 52

#Creo banca

cartasjugador = []
cartasbanca = []

#Comienzamos a repartir cartas al jugador

def cogeprimeracarta():
    global numerodecartas
    nrandom = random.randint(1, len(listacartas))
    darcartaaljugador = listacartas.pop(nrandom)
    print("Le ha salido la siguiente carta: " + str(darcartaaljugador))
    cartasjugador.append(darcartaaljugador)
    numerodecartas -= 1
    print(cartasjugador)

def cogesegundacarta():
    global numerodecartas
    nrandom = random.randint(1, len(listacartas))
    darcartaaljugador = listacartas.pop(nrandom)
    print("Le ha salido la siguiente carta: " + str(darcartaaljugador))
    cartasjugador.append(darcartaaljugador)
    nrandom = random.randint(1, len(listacartas))
    darcartaaljugador = listacartas.pop(nrandom)
    print("Le ha salido la siguiente carta: " + str(darcartaaljugador))
    cartasjugador.append(darcartaaljugador)
    numerodecartas -= 2
    print(cartasjugador)

#Comenzamos a repartir cartas a la banca

def bancaprimeracarta():
    global numerodecartas
    nrandom = random.randint(1, len(listacartas))
    darcartaalabanca = listacartas.pop(nrandom)
    cartasbanca.append(darcartaalabanca)
    numerodecartas -= 1

def bancasegundacarta():
    global numerodecartas
    nrandom = random.randint(1, len(listacartas))
    darcartaalabanca = listacartas.pop(nrandom)
    cartasbanca.append(darcartaalabanca)
    nrandom = random.randint(1, len(listacartas))
    darcartaalabanca = listacartas.pop(nrandom)
    cartasbanca.append(darcartaalabanca)
    numerodecartas -= 2

#Función para plantarse

def plantarse():
    puntosjugador = sum(cartasjugador)
    puntosbanca = sum(cartasbanca)
    if puntosbanca > 21 and puntosjugador < 21:
        print("¡Ha ganado!, su puntuación ha sido de " + str(puntosjugador) + " puntos, la banca obtenido  " + str(puntosbanca) + " puntos.")
    elif puntosjugador > 21:
        print("Ha perdido, su puntuación ha sido de " + str(puntosjugador) + " puntos, la banca ha obtenido " + str(puntosbanca) + " puntos.")
    elif puntosjugador < puntosbanca <= 21:
        print("Ha perdido, su puntuación ha sido de " + str(puntosjugador) + " puntos, la banca ha obtenido " + str(puntosbanca) + " puntos.")
    elif puntosjugador > puntosbanca and puntosjugador <= 21:
        print("¡Ha ganado!, su puntuación ha sido de " + str(puntosjugador) + " puntos, la banca obtenido  " + str(puntosbanca) + " puntos.")
    elif puntosjugador == puntosbanca:
        print("Ha empatado la partida con la banca.")
    sys.exit()

#Desarrollo del juego

def partidabanca():
    if sum(cartasbanca) >= 16:
        plantarse()

def partida():
    print("Quedan " + str(numerodecartas) + " cartas.")
    print("¿Qué desea hacer? 1: tomar otra carta 2: plantarse")
    decision = int(input())
    if decision == 1:
        print()
    elif decision == 2:
        plantarse()
    while decision != 2:
        cogeprimeracarta()
        partidabanca()
        partida()

print("Comienza la partida")
cogesegundacarta()
bancasegundacarta()
print(cartasjugador)
partida()
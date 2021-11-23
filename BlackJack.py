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
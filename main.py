from logica.logica import juego
import random

opcion = ''

while opcion != 3:
    opcion = input("Ingrese la opcion (1 para juego, 2 para salir): ")

    if opcion == '1':
        print("bienvenido")
        opciones = ['piedra', 'papel', 'tijera']
        usuario = input("Elige una opcion(piedra,papel o tijera): ")

        if usuario in opciones:
            computadora = random.choice(opciones)
            juego(usuario,computadora)
        else:
            print("opcion invalida, vuelve a intentarlo")


    elif opcion == '2':
        print("saliendo del programa adios!")
        break #sale del while y termina el flujo de ejecucion
    else:
        print("vuelve a elegir")


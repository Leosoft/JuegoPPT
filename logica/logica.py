
def juego(usuario,computadora):
    print(f"Tu elegiste: {usuario}")
    print(f"La computadora eligio: {computadora}")


    if usuario == computadora:
        print("Es un empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
            (usuario == "papel" and computadora == "piedra") or \
            (usuario == "tijera" and computadora == "papel"):
        print("GANASTE!!!!")
    else:
        print("La computadora gana")
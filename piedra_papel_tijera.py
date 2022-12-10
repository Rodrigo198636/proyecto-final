import random

class piedra_papel_tijera:
    
    def __init__(self) :
        pass
    def juego(self):

            opciones=["piedra", "papel", "tijera"]
            sep="-" *15


            jugador= input("seleccione piedra, papel o tijera: ").lower()
    
            computadora = random.choice(opciones)
            print(f"la computadora selecciono {computadora}")
            if jugador == computadora:
                print(f"empate!!, seleccionaron lo mismo{jugador}")
            elif jugador=="piedra" and computadora=="tijera":
                print(f"Ganaste!, {jugador} le gana a {computadora}")    
            elif jugador=="piedra" and computadora=="papel":
                print(f"Perdiste!, {computadora} le gana a {jugador}")    
            elif jugador=="papel" and computadora=="tijera":
                print(f"Perdiste!, {computadora} le gana a {jugador}")    
            elif jugador=="papel" and computadora=="piedra":
                print(f"Ganaste!, {jugador} le gana a {computadora}")    
            elif jugador=="tijera" and computadora=="papel":
                print(f"Ganaste!, {jugador} le gana a {computadora}")    
            elif jugador=="tijera" and computadora=="piedra":
                print(f"Perdiste!, {computadora} le gana a {jugador}")    
            print(f"{sep}Fin del juego{sep}")    
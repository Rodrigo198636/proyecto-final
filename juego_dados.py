import random

class juego_dados:
    
    def __init__(self) :
        pass
    def dado(self):




      while True:
        jugador=random.randint(1,6)

        computadora=random.randint(1,6)

        print('El jugador saco: ', jugador)

        print('la computadora saco: ', computadora)

        if jugador==computadora:
          print("Empate!!")

        elif jugador>computadora:
          print("Ganaste!!")    
        else:
          print("Perdiste!!")  
        break  

    

import random
class adivina_el_numero:
    
    def __init__(self) :
        pass
    def numero(self):

        adivina=random.randint(1,4)

        while True:
            numero=int(input("ingresa un nuero entre 1 y 4: "))
            if numero<=0:
                print("numero invalido")
            elif numero>= 5:
                print("numero invalido")
            elif numero != adivina:
                print("Perdiste, intentalo de nuevo")
            elif numero == adivina:
                print("Ganaste!!")
                
            break
            print("fin del juego")    
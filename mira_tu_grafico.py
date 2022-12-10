import matplotlib.pyplot as plt
import numpy as np
class Grafico:
    
    def __init__(self) :
        pass
    def grafico(self):

        Hinchas_boca=int(input("Cuantos hinchas de Boca hay en tu familia: "))
        Hinchas_river=int(input("Cuantos hinchas de River hay en tu familia: "))

        total= Hinchas_boca + Hinchas_river

        Boca = (Hinchas_boca/total) * 100
        River = (Hinchas_river/total) * 100

        print("En tu familia hay", Boca, " %" "hinchas de Boca")
        print("En tu familia hay", River, "% " "hinchas de River")

        valores= (Boca, River)
        etiquetas= ("hinchas de Boca", "Hinchas de River")
        plt.pie(valores, labels=etiquetas)
        plt.title("Porcentaje de Hinchada familiar")
        plt.tight_layout()
        plt.show()


import piedra_papel_tijera 
import mira_tu_grafico 
import adivina_el_numero 
import juego_dados 

while True:
        print("Bienvenido a tus juegos favoritos!!")
        print("Por favor, ingresa el juego que deseas jugar, o realiza un grafico con la opcion 'B'")
        actividad=str(input("A = juego, B = grafico, C= adivina, D= dados: "))   

        if actividad == "A":
            juego= piedra_papel_tijera.piedra_papel_tijera()
            juego.juego()
        elif actividad == "B":
            grafico = mira_tu_grafico.Grafico()
            grafico.grafico()
        elif actividad == "C":
            adivina =adivina_el_numero.adivina_el_numero()
            adivina.numero()
        elif actividad == "D":
            dados = juego_dados.juego_dados()
            dados.dado()
        else:
            print("Actividad invalida")   
        break  

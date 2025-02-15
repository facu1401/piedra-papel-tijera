import time
import random

PuntajeCompu = 0
Mipuntaje = 0

while True:
    misopciones = int(input("¿Qué opción eliges?:piedra(1) 🧶, papel(2) 📋 o tijera(3) ✂ ") )
    computadora = random.randint(1, 3)
    
    if misopciones == 1:
        print("Elegiste piedra")
    if misopciones == 2:
        print("Elegiste papel")
    if misopciones == 3:
        print("Elegiste tijera")
    
      
    
    if computadora == 1:
        print("Computadora eligió piedra")
    if computadora == 2:
        print("Computadora eligió papel")
    if computadora == 3:
        print("Computadora eligió tijera")
    
    #empate
    if misopciones == computadora: 
        print("Esto es un empate 😲")
        
    
    if (misopciones==1 and computadora==2):
         print("Has perdido 👿")
    if (misopciones==1 and computadora==3): 
        print("Has ganado 🥳")
      
    
    if (misopciones==2 and computadora==1):
         print("Has ganado 😁")
    if (misopciones==2 and computadora==3): 
        print("Has perdido 🤕")
       
        
    if (misopciones==3 and computadora==1):
         print("Has perdido 🥴")
    if (misopciones==3 and computadora==2): 
        print("Has ganado 🤩")

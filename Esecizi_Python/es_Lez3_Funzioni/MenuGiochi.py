#Costruisci un menu con i seguenti giochi
#1. Dadi
#2. Impiccato
#3. FizzBuzz (Stampa i numeri da 1 a 100. Accanto ai numeri multipli di 3 stampa fizz, accanto ai numeri multipli di 5 stampa Buzz, accanto a i numeri multipli di 3 e 5 stampa Fizz Buzz)

#Sviluppa ogni gioco in un file con script a parte 

import FizzBuzz


def avvia_Menu():
    #Qui faccio il match case per la scelta del gioco 
    FizzBuzz.avvia_Fizz_Buzz()

avvia_Menu()
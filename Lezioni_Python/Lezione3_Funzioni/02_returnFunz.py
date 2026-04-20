# Funzioni con return
#Le funzioni possono restituirci un valore in "uscita". Questo valore va "raccolto", può essere raccolto in un print o in un'altra variabile

def somma(x,y):
    somma = x + y
    return somma

risultato = somma(5, 8) #salvo il valore di return dentro una variabile
print("Il risultato della somma vale", risultato)
print("Il risultato della somma vale", somma(9,5))


def fai_calcolo(x, y, moltiplicatore):
    sommaInterna = somma(x, y)
    risultato = sommaInterna * moltiplicatore
    return risultato

risultato_finale = fai_calcolo(10, 5, 6)
print("Il tuo risultato finale vale", risultato_finale)
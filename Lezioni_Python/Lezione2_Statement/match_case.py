#Il Match Case controlla il valore di una variabile e non una condizione boolean
#Il Match Case in altri linguaggi è chiamato switch
giorno = "lunedì"

match giorno:
    case "lunedì":
        print("Buon inizio settimana")
    case "martedì":
        print("E' solo il secondo giorno della settimana")
    case "venerdì":
        print("Oggi è l'ultimo giorno di lavoro")
    case "mercoledì" | "giovedì":
        print("Sei esattamente a metà, tieni duro")
    case "sabato" | "domenica":
        print("Buon weekend, anche mezzi rotti")
    case _:
        print("Non ho capito che giorno è oggi")


## Posso aggiungere un if come valore di "guardia" all'interno di un case
voto = 60

match voto:
    case v if v >= 90: #Questa v si chiama variabile di catura. A v viene assegnato il valore di voto
        print("Ottimo")
    case v if v >= 70:
        print("Buono")
    case v if v >= 50:
        print("Sufficiente")
    case _:
        print("Insufficiente")
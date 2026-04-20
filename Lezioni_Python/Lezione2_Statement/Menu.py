import random

print("=== MENU GIOCHI ===")
print("Seleziona il gioco inserendo un numero")

scelta = ""

while scelta != 4:
    print("1. Gioco dei dadi")
    print("2. Gioco dell'impiccato")
    print("3. Gioco Wordle")
    print("4. ESCI")

    scelta = int(input("Inserisici un numero per scegliere: \n"))
    if scelta == 1:
        print("Hai scelto di giocare ai dadi")
        uscitaDadi = False
        while not uscitaDadi:
            facce = int(input("Quante facce hanno i tuoi dadi ?"))

            dado1 = random.randint(1, facce)
            dado2 = random.randint(1, facce)

            print(f"Dado1: {dado1}\nDado2: {dado2} ")
            if dado1 == dado2:
                print("Hai vinto")
            else:
                print("Hai perso")
            
            sceltaUserDadi = input("Vuoi continuare a giocare ? S/N")
            if(sceltaUserDadi == "S" or sceltaUserDadi == "s"):
                uscitaDadi = False
            else:
                uscitaDadi = True
                break

    elif scelta == 2:
        print("Hai scelto il gioco dell'impiccato")

    elif scelta == 3:
        print("Hai scelto Wordle")

    elif scelta == 4:
        print("Ciao, alla prossima")
        break
    else:
        print("Non ho capito la tua scelta")

print("Programma terminato")
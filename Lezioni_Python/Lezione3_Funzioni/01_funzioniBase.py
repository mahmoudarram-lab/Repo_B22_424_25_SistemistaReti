#FUNZIONI: blocco di codice riutilizzabile che permette di eseguire a comando delle istruzioni. Le funzioni possono essere richiamate da qualsiasi punto del codice 

#SINTASSI
#Dichiaro la funzione
def nome_funzione():
    #corpo funzioni
    nomeUser = input("Come ti chiami ?") #Questa è una variabile locale. Vive solo nella funzione nella quale è dichiarata
    print(f"Ciao {nomeUser}")

#Richiamo la funzione
# nome_funzione()

#Posso richiamare una funzione all'interno di altra funzione
def altra_funzione():
    print("Sono l'altra funzione. Ora richiamerò la prima")
    nome_funzione() #Sto richiamando la prima funzione

altra_funzione()


# Una funzione può avere dei parametri in ingresso
def salutaUser(nomeUser, etaUser):
    print(f"Ciao {nomeUser}, hai {etaUser} anni")

nomeInput = input("Come ti chiami ? ")
etaInput = input("Quanti anni hai ?")

salutaUser(nomeInput, etaInput)
salutaUser("Amedeo", 35)

nomi_studenti = ["Mandeep", "Amedeo", "Karin", "Vitoria"]

def salutaStudente(nome):
    return f"Ciao {nome}" # Mi sto facendo restituire una stringa

for nome in nomi_studenti:
    salutaStudente(nome)
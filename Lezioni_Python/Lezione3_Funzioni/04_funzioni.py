import random


#Dichiaro la funzione 
def benvenuto():
    print("ciao Dario")
    numerocasuale = random.randint(0, 101)
    print(f"Oggi il tuo numero è il {numerocasuale}")

#eseguo la funzione 
benvenuto()


# Le funzioni possono avere dei parametri in ingresso 
def descrivi_server(nome, ip):
    print(f"server: {nome} - IP: {ip}")


descrivi_server("Webserver", "192.168.1.20")
descrivi_server("DBServer", "192.168.1.10")
descrivi_server("BEServer", "192.168.1.25")

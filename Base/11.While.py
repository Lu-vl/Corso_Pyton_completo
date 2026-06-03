''' # While esegue un blocco di codice finchè la condizione è True
# esempio: 
    while True:
        print("Ciao)

'''
contatore_valore = 1
while contatore_valore <= 5:
    print(f"Esecuzione programma: {contatore_valore}")
    contatore_valore = contatore_valore + 1


risposta = ''

while risposta != 'esci':
    risposta = input(f"Scrivi qualcosa: ")
    print(risposta)
print('Ciao')
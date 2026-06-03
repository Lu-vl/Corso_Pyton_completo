'''
Liste in python
Cos'è: strutture dati che permettono di salvare più dati insieme

Una lista può contenere:
    - Numeri
    - Stringhe
    - Boolean
    - Altre liste

servono quando dobbiamo gestire gruppi di dati
-------
ORDINATE, MODIFICABILE, PUò AVERE DUPLICATI

studenti = []
APPEND aggiunge valori nella lista
possiamo creare lista vuota e aggiungere elementi ogni volta
'''

Studenti = ["Mario,", "Luca", "Luigia", "Andrea", "Rudy"]
#print(Studenti)

# aggiungo studente nella lista
'''Studenti.append("Teresa")
print(Studenti)'''

# Condizione if(se) elif(altrimenti se) else(altrimenti)
'''
if Condizione:
    codice
else:
    codice
--------
if Condizione:
    codice
elif:
    codice
else:
    codice
'''
'''
cliente = input("Hai una prenotazione? ")
if cliente == "si":
    print("ok")
else:
    print("Non abbiamo posti disponibili")
'''
#........................... con elif:
'''
cliente = input("Hai una prenotazione? ")
if cliente == "si":
    print("ok")
elif cliente == "no":
    print("non abbiamo posti")
else:
    print("errore, devi rispondere (si o no)")
'''

'''costo_snack = 5
budget_cliente = input("Quanti soldi hai nel portafoglio? ")
budget = float(budget_cliente)

if budget >= costo_snack:
    print("Perfetto! Puoi comprare lo snack 🍬")
elif budget > 0 and budget <= 4.99:
    print("Peccato, i soldi  non bastano... 😕 scegli un altro snack ")
else:
    print("Sei al verde! Non puoi comprare nessuno snack 😫")'''

#print(Studenti[-1])

#rimuovere elementi
#Studenti.remove(Studenti[4])
#print(Studenti)

#Studenti.append("Teresa")
#print(Studenti)
#Studenti.remove("Teresa")
#print(Studenti)

# Modifica elementi
#Studenti[0] = "Kevin"
#print(Studenti[0])

# Luigia
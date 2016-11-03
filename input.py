# input da tastiera

# Per ottenere input dalla tastiera
# si possono usare le funzioni
# raw_input() e input()

print "Come ti chiami? "
name = raw_input()
print "Ciao", name


# Prima di chiedere input all'utente
# e' sempre buona norma stampare un messaggio
# per specificare cosa il programma si aspetta.
# Tale messaggio si chiama anche prompt.
# Nell'esempio precedente il prompt era la stringa "Come ti chiami? "
# 
# Siccome aggiungere un prompt e' un'operazione
# comune, la funzione raw_input() puo' anche
# essere invocata come in questo altro esempio:

name = raw_input("Come ti chiami? ")
print "Ciao", name


# Per l'input di numeri interi
# si puo' invece usare la funzione input().
# Si comporta allo stesso di modo di raw_input()
# solo che trasforma la stringa in ingresso in un intero
# (se possibile) prima di restituire tale valore.

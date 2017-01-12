import math

carburante=float(input("Carburante (in galloni): "))
coh=float(input("Consumo Orario (in galloni/h): "))
if carburante<0 or coh<0:
   print "Non hai inserito dati corretti."
else:
   ore = int(carburante/coh)
   resto= (carburante/coh) - ore
   minuti = resto*60
   secondi =( minuti - int(minuti))*60
   print "Tempo di volo: ",ore,"h",int(minuti),"m",int(secondi), "s"

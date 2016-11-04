import math

termX=input("Inserisci il termine in x: ")
termN=input("Inserisci il termine noto: ")

if termX != 0 and termN != 0: 
   ris =float (termN) / float (termX) * (-1.0)
   print "La soluzione dell'equazione e' x = ", ris
elif termX == 0 and termN !=0:
   print "L'equazione e' impossibile. "

elif termX != 0 and termN == 0:
   ris =float (termN) / float (termX)
   print "La soluzione dell'equazione e' x = ",ris



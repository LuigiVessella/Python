import math

termX=input("Inserisci il termine in x: ")
termN=input("Inserisci il termine noto: ")


if termX == 0 and termN ==0:
    print "L'equazione e' indeterminata.  "

elif termX == 0 and termN !=0:
    print "L'equazione e' impossibile. "

else:
    ris =float (termN) / float (termX) * (-1.0)
    print "La soluzione dell'equazione e' x = ",ris



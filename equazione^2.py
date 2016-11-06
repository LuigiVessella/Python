import math
termX2=input("Inserisci il coefficiente di x^2: ")
termX=input("Inserisci il coefficiente di  x^1: ")
termN=input("Inserisci il termine noto: ")
if termX==0 and termN==0: 
   print "E' un equazione monomia ax^2=0, e' verificata solo per x=0 "

elif termN == 0:
   ris1 = 0
   ris2 = (termX/termX2)*(-1.0)
   print "Le soluzioni sono: ", ris1, "e ", ris2

elif termX == 0:
   ris = math.sqrt(((termN/termX2)*(-1.0)))
   print "La soluzione e': ", ris

else:
    delta=pow(termX,2) - 4.0*(termX2*termN)
    ris=(((termX*(-1))+ math.sqrt(delta)))/(2*termX2)
    ris2=(((termX*(-1))- math.sqrt(delta)))/(2*termX2)
    print "Le soluzioni sono: ",ris, "e ", ris2



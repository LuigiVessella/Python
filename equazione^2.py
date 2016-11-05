import math
termX2=input("Inserisci il termine in x^2: ")
termX=input("Inserisci il temrine in x^1: ")
termN=input("Inserisci il termine noto: ")
if termX==0 and termN==0: 
   print "L'equazione e' impossibile. "

elif termN == 0:
   ris1 = 0
   ris2 = (termX/termX2)*(-1.0)
   print "Le soluzioni sono: ", ris1, " ", ris2

elif termX == 0:
   ris = math.sqrt((termX2/termN)*(-1.0))
   print "La soluzione e': ", ris

else:
    delta=pow(termX,2) - 4.0*(termX2*termN)
    ris=(((termX*(-1))+ math.sqrt(delta)))/(2*termX2)
    ris2=(((termX*(-1))- math.sqrt(delta)))/(2*termX2)
    print "Le soluzioni sono: ",ris, " ", ris2



def tempsEnSeconde (temps) : 
    a = temps [0] * 24 * 60 * 3600
    b = temps [1] * 3600
    c = temps [2] * 60
    d = temps [3]
    sortie = a + b + c +  d 
    return sortie 
    pass
temps = (3,23,1,34)
print (type(temps))
print (tempsEnSeconde (temps)) 
def secondeEnTemps (seconde) :
    e = seconde % 31536000
    g = e % 86400
    h = g % 24
    j = h % 60
    k = seconde % 60
    sortie = e,g, h, j , k
    return sortie 
    pass
temps = secondeEnTemps(100000) 
print (temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps [3],"secondes")
def affichetemps(temps) : 
    if temps [0] == 0 and temps [1] != 0 :
        print(temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
    elif temps [0] == 0 and temps [1] == 0 and temps [2] != 0 :
        print(temps[2],"minutes",temps[3],"secondes")
    elif temps [0] == 0 and temps [1] == 0 and temps [2] == 0 and temps [3]!= 0 :
        print(temps[3],"secondes")
    elif temps [0] == 0 and temps [1]== 0 and temps [2] == 0 and temps [3] == 0 :
       print("Aucun temps enregistré") 
    elif temps [1] == 0 and temps [2] != 0:
        print(temps[0],"jours",temps[2],"minutes",temps[3],"secondes")
    elif temps [1] == 0 and temps [2] == 0 and temps [3] !=0 : 
        print(temps[0],"jours", temps[3],"secondes")
    elif temps [1] == 0 and temps [2] == 0 and temps [3] == 0 :
        print(temps[0],"jours")
    elif temps [2] == 0 and temps [3] != 0 :
        print(temps[0],"jours",temps[1],"heures",temps[3],"secondes")
    elif temps [2] and temps [3] == 0 :
        print(temps[0],"jours",temps[1],"heures")
    elif temps [3] == 0 : 
        print(temps[0],"jours",temps[1],"heures",temps[2],"minutes")
    else : 
        print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
    pass 
affichetemps ((1,0,14,23))   
def sommeTemps (temps1,temps2) :
    sommejours = temps1 [0]+ temps2[0]
    sommeheures = temps1 [1] + temps2 [1] 
    sommeminutes = temps1 [2] + temps2 [2]
    sommesecondes = temps1 [3]+ temps2 [3]
    secondeEnTemps (698486)
    sortie = print ("sommeTemps =" , (sommejours,"jours",sommeheures,"heures",sommeminutes,"minutes",sommesecondes, "secondes") ) 
    return sortie
    pass
temps = secondeEnTemps (698486)
sommeTemps ((2,3,4,25),(5,22,57,1))
def tempsEnDate(temps) :
    temps [0]
    temps [1]
    temps [2]
    temps [3]
    sortie = print ("année",temps [0],"jour",temps[1],"heure",temps[2],"minute",temps[3])
    return sortie
    pass
temps = (1970,1,0,0,0)
print (tempsEnDate,(temps))
def afficheDate (date = -1) :
    secondeEnTemps(1000000000)
    sortie = print (secondeEnTemps(1000000000))
    return sortie
    pass
seconde = 1000000000
temps = secondeEnTemps (1000000000)
affichetemps (temps)
afficheDate (tempsEnDate(temps))
afficheDate (1970)
import time
#print (time.time ())
#print (time.gmtime(0))
#print (time.gmtime([1000000000]))

def verifie(liste_temps):
    _somme = 0
    for i in liste_temps [0] :
        _somme = 0 + i
        if liste_temps [0] > 48 or  _somme > 140 :
            print ("Charge horaire trop importante")
    for i in liste_temps [1] :
        _somme = 0 + i    
        elif liste_temps [1] > 48 or _somme > 140 :
            print ("Charge horaire trop importante")
    for i in liste_temps [2] :
        _somme = 0 + i
        elif liste_temps [2] > 48 or liste_temps [2] > 140 :
            print ("Charge horaire trop importante")
        elif liste_temps [3] > 48 or liste_temps [3] > 140 :
            print ("Charge horaire trop importante")
        else :
            print ("Charge horaire normal" )   
    sortie = verifie (liste_temps)
    return sortie
    pass

liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)
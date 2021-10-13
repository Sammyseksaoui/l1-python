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
    g = seconde % (3600*24)
    h = g % 24
    j = h % 60
    k = seconde % 60
    sortie = g, h, j , k
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
    temps [4]
    sortie = print ("tempsEnDate", (temps [0],temps[1],temps[2],temps[3],temps[4]))
    return sortie
    pass
temps = (1970,1,0,0,0)
print (tempsEnDate,(temps))
def afficheDate (date = -1) :

    pass

temps = secondeEnTemps (1000000000)
affichetemps (temps)
afficheDate (TempsEnDate(temps))
afficheDate ()
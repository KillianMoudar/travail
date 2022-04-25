# Création d'une liste de 100 entiers tirés au hasard entre 0 et 500
from random import randrange
liste = []
for i in range(100):
    liste.append(randrange(500))

print(liste)
##
##def recherche(liste, valeur):
##    for e in liste :
##        if e == valeur :
##            return True
##        return False
##test = recherche(liste,58)
##print(test)
##
##def recherche_indice(liste, valeur):
##    for i in range(len(liste)):
##        if liste[i] == valeur :
##            return i
##    return None
##killian = recherche_indice(liste,25)
##print(killian)
##
##def recherche_minimum(liste):
##    i = 0
##    res = liste[0]
##    while i < len(liste) :
##        if res > liste[i] :
##            res = liste[i]
##        i = i + 1
##    return res
##testb = recherche_minimum(liste)
##print(testb)
##
##def recherche_maximum(liste):
##    i = 0
##    res = liste[0]
##    while i < len(liste) :
##        if res < liste[i] :
##            res = liste[i]
##        i = i + 1
##    return res
##testc = recherche_maximum(liste)
##print(testc)

def moyenne(liste):
    somme = 0
    for c in liste :
        somme = somme + c
    return somme/len(liste)
testd = moyenne(liste)
print(testd)

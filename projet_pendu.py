from random import randint
def nettoyage_mot(mot):
    mot = mot.lower()
    mot = mot[0:len(mot)-1]
    accent = ['é','è','ê','ë','à','â','ù','û','ç','ô','ï','î']
    sans_accent = ['e','e','e','e','a','a','u','u','c','o','i','i']
    i = 0
    while i < len(accent):
        mot = mot.replace(accent[i], sans_accent[i])
        i = i + 1
    return mot

def tirage_au_sort(nom_fichier):
    fichier = open(nom_fichier,'r', encoding = 'utf8')
    for chiffre in range(randint(1,22274)):
        chaine = fichier.readline()
    fichier.close()
    return nettoyage_mot(chaine)
print(tirage_au_sort('dictionnaire.txt'))



def deja_choisie(lettre):
    """
    Description de la fonction : Ajoute dans LETTRES_DEJA_CHOISIES les lettres choisies par le joueur
    et affiche un message informant le joueur dans le cas où il choisit une lettre déjà proposée précédemment
    lettre (str) : lettre proposée par le joueur
    return (bool) : True si la lettre a déjà été choisié, False sinon
    MODIFICATION EN PLACE de LETTRES_DEJA_CHOISIES
    """
    global LETTRES_DEJA_CHOISIES
    if lettre in LETTRES_DEJA_CHOISIES:
        PRINT('lettre déja choisie')
        return True
    else:
        LETTRES_DEJA_CHOISIES = LETTRES_DEJA_CHOISIES + [lettre]
        return False 
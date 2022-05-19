#exercice 2
velo_1 = {"id" : 1210, "typ" : "electrique", "station" : "place d'Italie", "statut" : "en panne"}
velo_1["statut"] = "dispo"
print("dispo" in velo_1.values())

#exercice 2bis
velo_2 = {"id" : 4869, "typ" : "classique", "station" : "lycée Jean Rostand", "statut" : "en panne"}
velo_3 = {"id" : 2689, "typ" : "electrique", "station" : "place Chaptal", "statut" : "dispo"}
parc_velib = []
parc_velib.append(velo_1)
parc_velib.append(velo_2)
parc_velib.append(velo_3)

def recherche_velo(parc):
    """
    role : recherhce un velo dispo dans parc
    parc (liste de dictionnaire) : liste qui contient tous les velos du parc
    return (bool) : True si dispo et False sinon
    """
    for velo in parc:
        if "dispo" in velo.values():
            return True
    return False
print(recherche_velo(parc_velib))

def recherche_velo_V2(parc):
    """
    role : recherhce les lieux ou un velib est disponible
    parc (liste de dictionnaire) : liste qui contient tous les velos du parc
    return (bool) : les lieux si disponibles, None sinon
    """
    res = ()
    for i in range(len(parc)):
        if "dispo" in parc[i].values():
            res = res + (parc[i]["station"],)
    if res != ():
        return res
    return None
print(recherche_velo_V2(parc_velib))

#exercice 3
positions = {}
positions[(48.853585, 2.301490)] = "Paris"
positions[(11.611358, 43.147752)] = "Djibouti"
positions[(37.023113, -8.996601)] = "Fortaleza de Sao Vicente"
positions[(7.677989,-5.025387)] = "Bouaké"

def localisation_photo(GPS,dico):
    if GPS in dico.keys():
        return dico[GPS]
    return None
print(localisation_photo((37.023113, -8.996601),positions))

#exercice 4
def lecture(nom_fichier):
    """
    description : ouvre un fichier texte et renvoie son contenu sous la forme d'une chaîne de caractère
    paramètre nom_fichier(str) : nom du fichier
    return (str) : contenu du fichier
    """
    with open(nom_fichier,'r') as fichier:
        return fichier.read()

def nb_de_fois(lettre,chaine):
    i = i + 1
    valeur = 0
    while i <= len(chaine) - 1:
        if chaine[i] == lettre:
            valeur = valeur + 1
        i = i + 1
    
def occurence(chaine):
    
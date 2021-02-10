# Paul QUIQUE - Joseph FLORET

from etudiants import L_ETUDIANTS

# --- --- ---Travail préliminaire

def pour_tous(liste):
    """
    :param liste: (list) une liste de booléens
    :return: (bool) un booléen (True|False)
    :Side-Effect: Renvoie False si la liste
    contient un élément False, True sinon.
    :CU: Aucune
    :Exemples:
    >>> pour_tous([])
    True
    >>> pour_tous((True, True, True))
    True
    >>> pour_tous((True, False, True))
    False
    """
    if len(liste) == 0:
        return True
    #Drapeau pour savoir si un élément False est trouvé
    flag = True
    i = 0
    
    #Remplacement du for + return par un while
    while (i < len(liste) and flag):
        if not liste[i]:
            flag = False
        i += 1
    return flag

def il_existe(liste):
    """
    :param liste: (list) liste une liste de booléens
    :return: (bool) True si la liste
    contient un élément True, False sinon.
    :CU: Aucune
    :Exemples:
    >>> il_existe([])
    False
    >>> il_existe((False, True, False))
    True
    >>> il_existe((False, False))
    False
    """
    if len(liste) == 0:
        return False
    #Drapeau pour savoir si un élément True est trouvé
    flag = False
    i = 0
    
    #Remplacement du for + return par un while
    while (i < len(liste) and not flag):
        if liste[i]:
            flag = True
        i += 1
    return flag

# --- --- --- Question 0
COURTE_LISTE = L_ETUDIANTS[:10]

# --- --- --- Question 1
def est_liste_d_etudiants(x):
    """
    :param x: (object) x un objet quelconque
    :return: (bool) un booléen (True|False)
    :Side-Effect: Renvoie True si x est une liste
    de dictionnaires avec les clés définies.
    :CU: Aucune
    :Exemples:
    >>> est_liste_d_etudiants(COURTE_LISTE)
    True
    >>> est_liste_d_etudiants("Timoleon") 
    False
    >>> est_liste_d_etudiants([('12345678', 'Calbuth', 'Raymond', 'Danse', '12') ])
    False
    >>> est_liste_d_etudiants([('nip', 'test_nip', 'nom', 'prenom', 'groupe') ])
    False
    >>> est_liste_d_etudiants([{'nip': 'test_nip', 'nom': 'test_nom', 'prenom': '...', 'formation': '...', 'groupe': '...'}])
    True
    """
    # Dans le cas ou x n'est pas une liste
    if not(isinstance(x, list)):
        return False
    keys = ['nip', 'nom', 'prenom', 'formation', 'groupe']
    for etudiant in x:
        # Dans le cas etudiant ou n'est pas un dictionnaire
        if not(isinstance(etudiant, dict)):
            return False
        # Vérifier la présence de chaque clé dans le dict
        for key in keys:
            if not(key in etudiant):
                return False
    return True

# --- --- --- Question 2
# On détermine la taille de la liste L_ETUDIANTS

# Sa taille est de :
NBRES_FICHES = len(L_ETUDIANTS)

# --- --- --- Question 3
# On déclare une variable entière contenant notre
# numéro étudiant:

NIP = 42017486

# On calcule le modulo NBRES_FICHES de NIP
# et on détermine la fiche associée

FICHE_ASSO = L_ETUDIANTS[NIP % NBRES_FICHES]

# Optionnel : afficher via print(FICHE_ASSO)

# --- --- --- Question 4

def liste_des_formations(liste):
    #Ce que doit faire la fonction n'est pas clair
    """
    :param liste: (list) liste une liste d'étudiants
    :return: (list) une liste de chaînes de
    caractères donnant les formations dans les
    fiches d'étudiants
    :Side-Effect: Renvoie une liste qui contient
    les formations de la liste en paramètre.
    :CU: est_liste_d_etudiants(liste) == True
    :Exemples:
    >>> sorted(liste_des_formations(COURTE_LISTE[:4])) == sorted(['SESI', 'PEIP', 'SESI', 'MASS'])
    True
    >>> sorted(liste_des_formations(COURTE_LISTE[0:2])) == sorted(['PEIP', 'SESI'])
    True
    """
    # Liste des formations à retourner
    formations = []
    
    # Extraire la formation de chaque étudiant
    # et l'ajouter à la liste des formations.
    for fiche in liste:
        formations.append(fiche['formation'])
    
    return formations

# --- --- --- Question 5

# On nomme la fonction occurrences_prenoms
# car elle retourne un dictonnaire qui à p
# -artir d'une clé prénom permet de conna
# ître le nombre d'étudiants de la liste avec
# ce prénom.

# Par ailleurs, cette fonction nécessite de
# parcourir une fois la liste en paramètre.

def occurrences_prenoms(liste):
    """
    :param liste: (list) liste une liste d'étudiants
    :return: (dict)  un dictionnaire avec une
    clé chaîne de caractère (str) et une valeur entière (int)
    :Side-Effect: Renvoie un dictionnaire qui
    associe à chaque prénom le nombre d'étudiants
    qui possèdent ce prénom.
    :CU: est_liste_d_etudiants(liste) == True
    :Exemples:
    >>> occurrences_prenoms(COURTE_LISTE[:5])['Anne'] == 1
    True
    >>> occurrences_prenoms(COURTE_LISTE)['David'] == 2
    True
    """
    # Créer un dictionnaire vide
    res = {}
    # Itérer sur la liste et stocker
    # l'étudiant courant dans etud
    for etud in liste:
        # Récupérer le prénom de l'étudiant
        prenom = etud['prenom']
        if prenom in res:
            # Augmenter de 1 le nombre d'étudiants
            # qui possèdent ce prénom
            res[prenom] = res[prenom] + 1
        else:
            # Initialiser à 1 le nombres d'étudiants
            # qui possèdent le prénom
            res[prenom] = 1
    return res

# Pour connaître le nombres d'étudiants pré-
# -nommés Camille et Alexandre:

app = occurrences_prenoms(L_ETUDIANTS)

nbCamille = 0
nbAlexandre = 0

if 'Camille' in app:
    nbCamille = app['Camille']
# nbCamille vaut 3 quand on l'affiche dans la console

if 'Alexandre' in app:
    nbAlexandre = app['Alexandre']
# nbAlexandre vaut 4 quand on l'affiche dans la console

# --- --- --- Question 6

# Pour connaître le nombre de prénoms différents,
# il faut évaluer la taille du dictionnaire.

nbPrenoms = len(app)
# Il y a 199 prénoms différents dans l'échantillon.

# --- --- --- Question 7

# Pour connaître le/les prénom(s) le/les plus
# fréquent(s), il faut itérer deux fois sur le
# dictionnaire:

max = 0
prenoms = []

# Dans un premier temps, on détermine le nombre
# d'occurences maximum

for cle in app:
    if app[cle] > max:
        max = app[cle]

# Dans un second temps on ajoute à la liste
# de prénoms tous ceux dont le nombre d'occ
# -urences est égal à max

for cle in app:
    if app[cle] == max:
        prenoms.append(cle)
        
# Les prenoms qui apparaissent le plus sont
# contenus dans prenoms, ce sont :
# ['Paul', 'Christiane', 'David', 'Margot', 'Marguerite', 'Guy', 'Frédéric']

# --- --- --- Question 8

def occurrences_nip(liste):
    """
    :param liste: (list) liste une liste d'étudiants
    :return: (dict) un dictionnaire avec une
    clé chaîne de caractère et une valeur entière
    :Side-Effect: Renvoie un dictionnaire qui
    associe à chaque nip le nombre d'occurences
    de ce code nip dans la liste.
    :CU: est_liste_d_etudiants(liste) == True
    :Exemples:
    >>> occurrences_nip(COURTE_LISTE[:5])['49284201'] == 1
    True
    >>> occurrences_nip(COURTE_LISTE)['48686474'] == 2
    False
    """
    # Créer un dictionnaire vide
    res = {}
    # Itérer sur la liste et stocker
    # l'étudiant courant dans etud
    for etud in liste:
        # Récupérer le nip de l'étudiant
        nip = etud['nip']
        if nip in res:
            # Augmenter de 1 le nombre d'étudiants
            # qui possèdent ce prénom
            res[nip] = res[nip] + 1
        else:
            # Initialiser à 1 le nombres d'étudiants
            # qui possèdent le prénom
            res[nip] = 1
    return res

# On peut vérifier que pour chaque nip
# le nombre d'occurences est de 1
# exactement

nips_distincts = True
nips = occurrences_nip(L_ETUDIANTS)

for cle in nips:
    if not(nips[cle] == 1):
        nips_distincts = False
        break
    
# Enfin, on vérifie que tous les nips sont distincts
# print(nips_distincts)
# True -> Donc tous les nips sont différents!

# --- --- --- Question 9

# Il ne faut pas utiliser de chaines litérales.
# On pourra consulter le nombre d'étudiants par
# formations en utilisant dans_la_formation['formation']

dans_la_formation = {}

# Liste qui contient la formation propre à chaque
# étudiant

l_formations = liste_des_formations(L_ETUDIANTS)

for formation in l_formations:
    # Si la clé existe, incrémenter la valeur associée de 1
    if formation in dans_la_formation:
        dans_la_formation[formation] += 1
    # Si la clé n'existe pas, l'associer à la valeur 1
    else:
        dans_la_formation[formation] = 1

# On peut maintenant accéder au nombre d'étudiants
# dans un formation :

etudiants_en_sesi = dans_la_formation['SESI']

# ou bien afficher les statistiques complètes avec:
# print(dans_la_formation)
# >>> {'SESI': 373, 'PEIP': 124, 'MASS': 67, 'LICAM': 19}

# --- --- --- Question 10

def liste_formation(liste, form):
    """
    :params liste, form: liste – (list) une liste de fiches d’étudiants
                form – (str) une formation
    :return: (list) une liste de quatre paramètres
    :Side-Effect: (list) la liste des étudiants de la formation
    form sous forme d’un quadruplet (nip, nom, prenom, groupe
    :CU: Aucune
    :Exemples:
    >>> l_SESI = liste_formation(COURTE_LISTE, 'SESI')
    >>> len(l_SESI)
    6
    >>> type(l_SESI[1]) == tuple and len(l_SESI[1]) == 4
    True
    >>> len(liste_formation(L_ETUDIANTS, 'INFO'))
    0
    """
    
    etudiants_dans_formation = []
    
    # Itérer sur la liste et évaluer la formation
    # de chaque étudiant, si c'est la formation passée
    # en paramètres, ajouter l'étudiant à la liste
    # des étudiants dans la formation.
    
    for fiche in liste:
        # Si la formation de la fiche est identique à celle passée
        # en paramètres:
        if fiche['formation'] == form:
            # Ajouter l'étudiant à la liste de retour
            etudiants_dans_formation.append((fiche['nip'], fiche['nom'], fiche['prenom'], fiche['groupe']))
            
    return etudiants_dans_formation

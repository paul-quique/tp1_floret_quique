from etudiants import L_ETUDIANTS

#Travail préliminaire

def pour_tous(liste):
    """
    Paramètres: liste une liste de booléens
    Valeur de retour: un booléen (True|False)
    Comportement: Renvoie False si la liste
    contient un élément False, True sinon.
    >>> pour_tous([])
    True
    >>> pour_tous((True, True, True))
    True
    >>> pour_tous((True, False, True))
    False
    """
    if len(liste) == 0:
        return True
    for i in liste:
        if not(i):
            return False
    return True

def il_existe(liste):
    """
    Paramètres: liste une liste de booléens
    Valeur de retour: un booléen (True|False)
    Comportement: Renvoie True si la liste
    contient un élément True, False sinon.
    >>> il_existe([])
    False
    >>> il_existe((False, True, False))
    True
    >>> il_existe((False, False))
    False
    """
    if len(liste) == 0:
        return False
    for i in liste:
        if i:
            return True
    return False

#Question 0
COURTE_LISTE = L_ETUDIANTS[:10]

#Question 1
def est_liste_d_etudiants(x):
    """
    Paramètres: x un objet quelconque
    Valeur de retour: un booléen (True|False)
    Comportement: Renvoie True si x est une liste
    de dictionnaires avec les clés définies.
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
    #Dans le cas ou x n'est pas une liste
    if not(isinstance(x, list)):
        return False
    keys = ['nip', 'nom', 'prenom', 'formation', 'groupe']
    for etudiant in x:
        #Dans le cas etudiant n'est pas un dictionnaire
        if not(isinstance(etudiant, dict)):
            return False
        for key in keys:
            if not(key in etudiant):
                return False
    return True

#Question 2
# On détermine la taille de la liste L_ETUDIANTS

#Sa taille est de :
NBRES_FICHES = len(L_ETUDIANTS)

#Question 3
#On déclare une variable entière contenant notre
#numéro étudiant:

NIP = 42017486

#On calcule le modulo NBRES_FICHES de NIP
#et on détermine la fiche associée

FICHE_ASSO = L_ETUDIANTS[NIP % NBRES_FICHES]
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

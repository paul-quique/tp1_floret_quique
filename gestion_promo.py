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



# Exo 1

def voisins_entrants(adj:list, x:int) -> list:
    tab = []
    for i in range(len(adj)):
        if x in adj[i]:
            tab.append(i)
    return tab

assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]

# Exo 2

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat

assert nombre_suivant('1211') == '111221'
assert nombre_suivant('311') == '1321'

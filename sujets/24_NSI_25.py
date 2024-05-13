# Exo 1

def recherche_min(tab:list) -> int:
    mini, indice = tab[0], 0
    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini, indice = tab[i], i
    return indice
    
assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2
assert recherche_min([-1, -2, -3, -3]) == 2

# Exo 2

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab)-1
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else:
            tab[gauche] = tab[droite]
            tab[droite] = 1
            droite = droite - 1
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Exo 1

def moyenne(tab:list) -> float:
    total = 0
    for f in tab:
        total += f
    return total / len(tab)

assert moyenne([1]) == 1.0
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert moyenne([1, 2]) == 1.5

# Exo 2

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab)
    while debut <= fin:
        m = len(tab)//2
        if x == tab[m]:
            return m
        if x > tab[m]:
            debut = m
        else:
            fin = m
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == False
assert dichotomie([], 28) == False

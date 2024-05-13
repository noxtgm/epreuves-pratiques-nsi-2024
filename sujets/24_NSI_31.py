# Exo 1

def multiplication(n1:int, n2:int) -> int:
    if n1 < 0 and n2 > 0:
        return -multiplication(-n1, n2)
    if n1 > 0 and n2 < 0:
        return -multiplication(n1, -n2)
    if n1 < 0 and n2 < 0:
        return multiplication(-n1, -n2)
    produit = 0
    for i in range(n1):
        produit += n2
    return produit

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0

# Exo 2

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False

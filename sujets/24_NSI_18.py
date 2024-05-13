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

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m+1, j) 
    elif tab[m] > x:
        return chercher(tab, x, i, m-1) 
    else:
        return m 

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2

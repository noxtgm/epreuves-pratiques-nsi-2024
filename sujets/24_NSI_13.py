# Exo 1

def recherche(elt:int, tab:list):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None

assert recherche(1, [2, 3, 4]) == None
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3

# Exo 2

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

assert insere([1, 2, 4, 5], 3) == [1, 2, 3, 4, 5]
assert insere([1, 2, 7, 12, 14, 25], 30) == [1, 2, 7, 12, 14, 25, 30]
assert insere([2, 3, 4], 1) == [1, 2, 3, 4]
assert insere([], 1) == [1]

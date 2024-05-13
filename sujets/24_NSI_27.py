# Exo 1

def couples_consecutifs(tab:list) -> list:
    tab = []
    for i in range(1, len(tab)):
        if tab[i-1] + 1 == tab[i]:
            tab.append((tab[i-1], tab[i]))    
    return tab

assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# Exo 2

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M): # propage en bas 
        colore_comp1(M, i, j+1, val) 

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

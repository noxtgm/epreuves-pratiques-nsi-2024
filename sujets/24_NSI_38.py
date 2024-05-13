# Exo 1

def indices_maxi(tab:list) -> tuple:
    maxi, indices = tab[0], [0]
    for i in range(1, len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indices = [i]
        elif tab[i] == maxi:
            indices.append(i)
    return (maxi, indices)

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])

# Exo 2

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse

def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        n = pile.pop()
        if n >= 0:
            pile_positifs.append(n)
    return renverse(pile_positifs)

assert renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positifs([-2]) == []

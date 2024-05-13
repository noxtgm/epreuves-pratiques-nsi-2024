# Exo 1

def moyenne(notes:list) -> int:
    total, coef = 0, 0
    for n in notes:
        total += n[0] * n[1]
        coef += n[1]
    return total / coef

assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5

# Exo 2

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1] 
    for i in range(1, len(ligne)): 
        ligne_suiv.append(ligne[i-1] + ligne[i]) 
    ligne_suiv.append(1) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(1, n+1): 
        ligne_k = ligne_suivante(triangle[k-1])
        triangle.append(ligne_k)
    return triangle

assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

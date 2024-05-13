# Exo 1

def occurrences(caractere:str, chaine:str):
    nb = 0
    for c in chaine:
        if c == caractere:
            nb += 1
    return nb

assert occurrences('e', "sciences") == 2
assert occurrences('i',"mississippi") == 4
assert occurrences('a',"mississippi") == 0

# Exo 2

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre: 
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang + 1) 

assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291,1) == [50, 50, 50, 50, 50, 20, 20, 1]

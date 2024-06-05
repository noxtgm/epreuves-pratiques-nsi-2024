# Exo 1

def recherche_motif(motif:str, texte:str) -> list:
    liste = []
    indice = 0
    while indice < len(texte):
        if motif == texte[indice:indice+len(motif)]:
            liste  += [indice]
            indice += len(motif)
        else:
            indice += 1
    return liste

assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]

# Exo 2

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc

assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0) == [0, 1, 2, 3]
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4) == [4, 5]

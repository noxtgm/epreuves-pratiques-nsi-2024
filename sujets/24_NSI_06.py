# Exo 1

def verifie(tab:list) -> bool:
    if tab == []:
        return True
    else:
        nb = tab[0]
        for i in range(0, len(tab)):
            if nb > tab[i]:
                return False
            nb = tab[i]
        return True        

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([]) == True
assert verifie([5]) == True

# Exo 2

def depouille(urne:list):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

assert depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}
assert depouille([]) == {}

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax: 
            nmax = election[candidat]
    liste_finale = [ nom for nom in election if election[nom] == nmax ] 
    return liste_finale

election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])
assert election == {'A': 3, 'B': 4, 'C': 3}
assert vainqueurs(election) == ['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B']


# Exo 1

def recherche(tab:list, n:int) -> int:
    debut = 0
    fin = len(tab) -1
    while fin >= debut:
        m = (debut+fin) // 2
        if tab[m] == n:
            return m
        elif tab[m] > n:
            fin = m - 1
        else:
            debut = m + 1

assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == None

# Exo 2
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'









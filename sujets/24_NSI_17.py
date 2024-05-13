# Exo 1

def nb_repetitions(elt, tab:list) -> int:
    repetitions = 0
    for c in tab:
        if elt == c:
            repetitions += 1
    return repetitions

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44]) == 0

# Exo 2

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ""
    while a > 0:
        bin_a = str(a%2) + bin_a 
        a = a // 2
    return bin_a

assert binaire(0) == '0'
assert binaire(77) == '1001101'


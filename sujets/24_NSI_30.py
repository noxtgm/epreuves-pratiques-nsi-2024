# Exo 1

def fusion(tab1:list, tab2:list) -> list:
    tab = []
    while tab1 != [] and tab2 != []:
        if tab1[0] < tab2[0]:
            tab.append(tab1.pop(0))
        else:
            tab.append(tab2.pop(0))
    if tab1 == []:
        tab += tab2
    if tab2 == []:
        tab += tab1
    return tab 

assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([], []) == []
assert fusion([1, 2, 3], []) == [1, 2, 3]

# Exo 2

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]: 
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIV") == 2024

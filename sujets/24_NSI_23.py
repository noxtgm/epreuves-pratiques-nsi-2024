# Exo 1

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

def insertion_abr(a:tuple, cle:int) -> tuple:
    if a == None:
        return (None, cle, None)
    if cle == a[1]:
        return a
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    else:
        return (insertion_abr(a[0], cle), a[1], a[2])

assert insertion_abr(abr1, 4) == ((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert insertion_abr(abr1, -5) == (((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert insertion_abr(abr1, 2) == ((None,0,None),1,(None,2,(None,3,None)))

# Exo 2

def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses: 
        i = 0
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] = boites[i] + masse 
    return nb_boites

assert empaqueter([1, 2, 3, 4, 5], 10) == 2
assert empaqueter([1, 2, 3, 4, 5], 5) == 4
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5

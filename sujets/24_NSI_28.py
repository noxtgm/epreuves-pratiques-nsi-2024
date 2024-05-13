# Exo 1

def fibonacci(n:int) -> int :
    F = [0,1]
    for i in range(2,n+1) :
        F.append(F[-1] + F[-2])
    return F[n]

assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025

# Exo 2

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] 

    for i in range(len(eleves)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
assert eleves_du_mois([],[]) == (0, [])










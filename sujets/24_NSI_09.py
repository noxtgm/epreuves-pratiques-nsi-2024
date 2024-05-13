# Exo 1

def effectif_notes(notes_eval:list) -> list:
    tab = [0] * 11
    for note in notes_eval:
        tab[note] += 1
    return tab

def notes_triees(effectifs:int):
    tab = []
    for i in range(len(effectifs)):
        for j in range(effectifs[i]):
            tab.append(i)
    return tab

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
assert eff == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
assert notes_triees(eff) == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]

# Exo 2

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: 
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

assert dec_to_bin(25) == '11001'
assert bin_to_dec('101010') == 42

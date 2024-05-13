# Exo 1

def annee_temperature_minimale(t_moy:list, annees:list):
    mini, indice = t_moy[0], 0
    for i in range(1, len(t_moy)):
        if mini > t_moy[i]:
            mini, indice = t_moy[i], i
    return (mini, annees[indice])

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)

# Exo 2

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True


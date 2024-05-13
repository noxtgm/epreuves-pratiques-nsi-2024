# Exo 1

def ou_exclusif(tab1:list, tab2:list) -> list:
    tab = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            tab.append(0)
        else:
            tab.append(1)
    return tab
    
assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]

# Exo 2

class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]
    
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])
                                   
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(1, self.ordre): 
            if self.somme_ligne(i) != s: 
                return False
                                   
        #test de la somme de chaque colonne 
        for j in range(self.ordre): 
            if self.somme_col != s: 
                return False
                                   
        return True



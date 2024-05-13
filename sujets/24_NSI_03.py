# Exo 1
def maximum_tableau(tab:list) -> int:
    max = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
            
    return max

assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131
assert maximum_tableau([-27, 24, -3, 15]) == 24

# Exo 2

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == '(': 
            p.empiler(c)
        elif c == ')': 
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert bon_parenthesage("((()())(()))") == True
assert bon_parenthesage("())(()") == False
assert bon_parenthesage("(())(()") == False

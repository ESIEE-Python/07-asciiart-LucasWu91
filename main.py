"""
Fichier main.py
"""
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractère

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    l=[]
    nombre=1
    for i in range(1, len(s)) :
        if s[i]==s[i-1] :
            nombre+=1
        else :
            l.append((s[i-1],nombre))
            nombre =1
    l.append((s[-1],nombre))
    # votre code ici
    return l

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument

    Args:
        s (str): la chaîne de caractère
        
    Returns:
    
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    if not s :
        return[]
    ini=s[0]
    nombre = 1
    while nombre < len(s) and ini==s[nombre] :
        nombre = nombre+1
    recursive=artcode_r(s[nombre:])
    return [(ini,nombre)] + recursive
#### Fonction principale


def main():
    """
    Test pour verifeir si les deux programmes sont bon
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

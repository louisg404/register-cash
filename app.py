class pays(object):
    def __init__(self, pays, code, tva):
        self.pays = pays
        self.code = code
        self.tva = tva

codesPays = []
codesPays.append(pays('France', 'FR', 20))
codesPays.append(pays('Espagne', 'ES', 21))
codesPays.append(pays('Italie', 'IT', 22))
codesPays.append(pays('Luxembourg', 'LU', 17))
codesPays.append(pays('Portugal', 'PT', 23))
codesPays.append(pays('Roumanie', 'RO', 19))

def menu():
    print("1. Afficher le tableau des pays")
    print("2. Rechercher un pays")
    print("3. Quitter")
    choix = input("Choisissez un element : ")
    if choix == 1:
        afficherTableau()
    elif choix == 2:
        rechercherPays()
    elif choix == 3:
        quitter()
    else:
        print("Aucun element ne correspond a votre recherche")
        retourMenu()

def retourMenu():
    choix = raw_input("Revenir au menu ?")
    menu()

def afficherTableau():
    print("-------------------------------")
    for item in codesPays:
        print item.pays, "(" + item.code + ")", "TVA :", item.tva
    print("-------------------------------")
    retourMenu()

def rechercherPays():
    paysUtilisateur = raw_input('Entrez un code pays : ')
    print(paysUtilisateur)
    for item in codesPays:
        if item.code == paysUtilisateur:
            print "Le code pays correspond au pays suivant :", item.pays, "(" + item.code + ")", "TVA :", item.tva
            totalHT = input('Entrez un montant HT : ')
            totalTTC = float(totalHT) + (float(item.tva) / 100 * float(totalHT))
            print "Le montant TTC est de", totalTTC
            retourMenu()
        else:
            print "Aucun pays ne correspond a votre recherche"
            retourMenu()

def quitter():
    exit

# Demarrage
menu()
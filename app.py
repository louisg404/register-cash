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

def afficherTableau():
    print("-------------------------------")
    for item in codesPays:
        print item.pays, "(" + item.code + ")", "TVA :", item.tva
    print("-------------------------------")

def calculerTtc():
    montantHt = raw_input('Entrez un montant HT : ')
    tauxTva = raw_input('Entrez un montant TVA : ')

    total = int(montantHt) + float(tauxTva)
    print(total)

# Demarrage
afficherTableau()
calculerTtc()
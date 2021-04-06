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
    class article(object):
        def __init__(self, quantite, prix):
            self.quantite = quantite
            self.prix = prix

    prix = raw_input('Entrez un montant HT : ')
    quantite = raw_input('Entrez une quantite : ')

    articles = []
    articles.append(article(quantite, prix))

    paysUtilisateur = raw_input('Entrez un code pays : ')
    for item in codesPays:
        if item.code == paysUtilisateur:
            for article in articles:
                totalTTC = float(article.prix) * int(article.quantite) * (1 + float(item.tva) / 100)
                print "Le montant TTC est de", totalTTC

# Demarrage
afficherTableau()
calculerTtc()
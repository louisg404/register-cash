class pays(object):
    def __init__(self, pays, code, tva):
        self.pays = pays
        self.code = code
        self.tva = tva

class reduction(object):
    def __init__(self, minimum, taux):
        self.minimum = minimum
        self.taux = taux

codesPays = []
codesPays.append(pays('France', 'FR', 20))
codesPays.append(pays('Espagne', 'ES', 21))
codesPays.append(pays('Italie', 'IT', 22))
codesPays.append(pays('Luxembourg', 'LU', 17))
codesPays.append(pays('Portugal', 'PT', 23))
codesPays.append(pays('Roumanie', 'RO', 19))

reductions = []
reductions.append(reduction(1000, 3))
reductions.append(reduction(5000, 5))
reductions.append(reduction(7000, 7))
reductions.append(reduction(10000, 10))
reductions.append(reduction(15000, 15))

def afficherTableau():
    print("-------------------------------")
    print("Pays")
    print("-----------")
    for item in codesPays:
        print item.pays, "(" + item.code + ")", "TVA :", item.tva
    print("-------------------------------")

def afficherReductions():
    print("Reductions")
    print("-----------")
    for item in reductions:
        print item.minimum, "(", item.taux, "%)"
    print("-------------------------------")

def calculerTtc():
    class article(object):
        def __init__(self, quantite, prix, libelle):
            self.quantite = quantite
            self.prix = prix
            self.libelle = libelle

    ajouter = 'o'
    articles = []
    totalHt = 0

    while ajouter == 'o':
        prix = raw_input('Entrez un montant HT : ')
        quantite = raw_input('Entrez une quantite : ')
        libelle = raw_input('Entrez un libelle : ')
        articles.append(article(quantite, prix, libelle))
        ajouter = raw_input("Ajouter un autre article ? (o/n)")

    paysUtilisateur = raw_input('Entrez un code pays : ')
    tauxADeduireHt = 0

    for item in codesPays:
        if item.code == paysUtilisateur:
            print("-------------------------------")
            for article in articles:
                totalHt = totalHt + (float(article.prix) * int(article.quantite))
                print article.libelle, "x" + article.quantite, ":", article.prix, "=", float(article.prix) * float(article.quantite)

            if totalHt >= 1000 and totalHt < 5000:
                tauxADeduireHt = 3
            elif totalHt >= 5000 and totalHt < 7000:
                tauxADeduireHt = 5
            elif totalHt >= 7000 and totalHt < 10000:
                tauxADeduireHt = 7
            elif totalHt >= 10000 and totalHt < 15000:
                tauxADeduireHt = 10
            elif totalHt >= 15000:
                tauxADeduireHt = 15

            totalTTC = (totalHt * (1 - float(tauxADeduireHt) / 100)) * (1 + float(item.tva) / 100)

            print("-------------------------------")
            print "Montant HT :", totalHt
            if tauxADeduireHt != 0:
                print "Reduction de : -", tauxADeduireHt, "% soit -", (totalHt / 100 * tauxADeduireHt)
            print "TVA de :", item.tva, "% soit", (totalTTC - (totalHt * (1 - float(tauxADeduireHt) / 100)))
            print("-------------------------------")
            print "Total TTC :", totalTTC

# Demarrage
afficherTableau()
afficherReductions()
calculerTtc()
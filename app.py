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
        def __init__(self, quantite, prix):
            self.quantite = quantite
            self.prix = prix

    ajouter = 'o'
    articles = []
    totalHt = 0

    while ajouter == 'o':
        prix = raw_input('Entrez un montant HT : ')
        quantite = raw_input('Entrez une quantite : ')
        articles.append(article(quantite, prix))
        ajouter = raw_input("Ajouter un autre article ? (o/n)")

    paysUtilisateur = raw_input('Entrez un code pays : ')
    tauxADeduireHt = raw_input('Entrez un taux de reduction : ')

    for item in codesPays:
        if item.code == paysUtilisateur:
            for article in articles:
                totalHt = totalHt + (float(article.prix) * int(article.quantite))

            if totalHt >= 1000 and totalHt < 5000:
                print("Reduction suggeree de 3%")
            elif totalHt >= 5000 and totalHt < 7000:
                print("Reduction suggeree de 5%")
            elif totalHt >= 7000 and totalHt < 10000:
                print("Reduction suggeree de 7%")
            elif totalHt >= 10000 and totalHt < 15000:
                print("Reduction suggeree de 10%")
            elif totalHt >= 15000:
                print("Reduction suggeree de 15%")

            totalTTC = (totalHt * (1 - float(tauxADeduireHt) / 100)) * (1 + float(item.tva) / 100)
            print "Le total TTC est de :", totalTTC

# Demarrage
afficherTableau()
afficherReductions()
calculerTtc()
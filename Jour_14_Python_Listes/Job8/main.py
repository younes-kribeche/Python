L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def somme_chiffres_paires(list):
    somme = 0
    for nombre in list:
        if nombre % 2 == 0:
            somme += nombre
    return somme

resultat = somme_chiffres_paires(L)
print(resultat)

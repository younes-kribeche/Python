import string

alphabet = string.ascii_lowercase

for lettre in range(1, 27*2):  # Boucle pour chaque étage de la pyramide
    lettres_affichees = alphabet[:lettre % 26:lettre]  # Sélectionne les premières lettres de l'alphabet
    print(lettres_affichees)
nom_DS = "Nintendo DS Lite"
nom_PS5 = "Playstation 5"
nom_GBA = "Game Boy Advance"

prix_DS = 248
prix_PS5 = 399
prix_GBA = 149

quantite_DS_en_stock = 7

prix_DS_inflation = prix_DS * (1.10)

print(f"Notre dernier produit: La {nom_DS}, est disponible pour {prix_DS_inflation}€. Dépêchez-vous il n'en reste que {quantite_DS_en_stock} en stock ! Vous pouvez aussi retrouver la toute dernière {nom_PS5} à seulement {prix_PS5}€ ainsi que l'indémodable {nom_GBA} au doux prix de {prix_GBA}€ ! Combien de consoles comptez-vous acheter:")
quantite_voulue = int(input("Quantité: "))
nouvelle_quantite = quantite_DS_en_stock - quantite_voulue

print("Vous avez commandé", quantite_voulue, "consoles, il en reste", nouvelle_quantite)

print(f"Notre dernier produit: La {nom_DS}, est disponible pour {prix_DS_inflation}€. Dépêchez-vous il n'en reste que {nouvelle_quantite} en stock ! Vous pouvez aussi retrouver la toute dernière {nom_PS5} à seulement {prix_PS5}€ ainsi que l'indémodable {nom_GBA} au doux prix de {prix_GBA}€ ! Combien de consoles comptez-vous acheter:")
quantite_voulue = int(input("Quantité: "))



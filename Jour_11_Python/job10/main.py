montant_initial_invest = 5000
taux_rend_annuel = 2
montant_total = montant_initial_invest * (1 + taux_rend_annuel/100)

print(f"Il vous reste {montant_total}€ sur votre compte.")
print("Combien voulez-vous retirer?")

montant_retire = montant_total * 0.1
print(f"Vous avez retiré {montant_retire}€.")

nouveau_montant_invest = montant_total - montant_retire
print(f"Il vous reste {nouveau_montant_invest}€.")

gain_annuel = montant_total - montant_initial_invest
print(f"Le montant de votre rendement annuel s'élève à {gain_annuel}€.")

nouveau_taux_annuel = taux_rend_annuel / 2
print(f"Au vu de votre dernier retrait, votre rendement annuel est passé à {nouveau_taux_annuel}%.")

nouveau_total_annuel = nouveau_montant_invest * (1 + nouveau_taux_annuel/100)
nouveau_rend_annuel = nouveau_total_annuel - nouveau_montant_invest 
print(f"Le montant de votre nouveau rendement annuel s'élève à {nouveau_rend_annuel}€.")




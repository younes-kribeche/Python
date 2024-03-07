def moyenne(note1, note2, note3):
    return((note1 + note2 + note3) / 3)

note1 = float(input("Veuillez entrer une première note: " ))
note2 = float(input("Veuillez entrer une deuxième note: " ))
note3 = float(input("Veuillez entrer une troisième note: " ))

moyenne_étudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_étudiant <= 20:
    print("Très bon élève")
if 11 <= moyenne_étudiant <= 14:
    print("Bon élève")
if 8 <= moyenne_étudiant <= 10:
    print("Élève moyen")
if 0 <= moyenne_étudiant <= 7:
    print("Élève devant faire des efforts")


    
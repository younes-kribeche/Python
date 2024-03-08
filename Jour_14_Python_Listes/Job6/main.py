liste = [1, 2, 3, 4, 5]

def swap(i):
    liste[0], liste[4] = liste[4], liste[0]
    print(liste)

swap(liste)
L = [8, 24, 48, 2, 16]

def programme():
    impairs = set()
    for i in L:
        if i % 3 == 0:
            impairs.add(i)
    print(len(impairs))

programme()
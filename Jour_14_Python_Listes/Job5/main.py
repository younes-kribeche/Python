L = [1, 2, 3, 4, 5]
print(L)
print(L[1])

def f(i):
    i[3] = L[2] + L[4]
    print(i)

f(L)

print(L[4])


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i):
        print(i)

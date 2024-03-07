for i in range(1, 101):
    Fizz = i % 3 == 0
    Buzz = i % 5 == 0

    if Fizz and Buzz:
        print("FizzBuzz")
    elif Fizz:
        print("Fizz")
    elif Buzz:
        print("Buzz")
    else:
        print(i)
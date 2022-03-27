def inner_factorial(number):
    if number <= 1:
        return 1
    aaa = inner_factorial(number - 1)
    print(aaa)
    return number * inner_factorial(number - 1)


print(inner_factorial(4))

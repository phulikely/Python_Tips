def cal_square(x):
    return x ** 2


test_num = cal_square(3)
print(test_num)


test_lambda = lambda x: x**2 if x > 2 else 1
print(test_lambda(2))
print(test_lambda(3))

from math import factorial

num_1 = int(input())
num_2 = int(input())


def factorial_num(num):
    result = factorial(num)
    return result


print(f"{(factorial_num(num_1) / factorial(num_2)):.2f}")

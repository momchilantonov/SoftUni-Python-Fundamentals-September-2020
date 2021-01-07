# Solution with loop

num = int(input())


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n-3):
        res.append(sum(res[-3:]))
    res = [str(el) for el in res]
    return res


print(f"{' '.join(tribonacci([1, 1, 2], num))}")

# Solution with recursion

# def trib_rec(n):
#     if n == 0 or n == 1 or n == 2:
#         return 1
#     elif n == 3:
#         return 2
#     else:
#         return trib_rec(n-1)+trib_rec(n-2)+trib_rec(n-3)
#
#
# def trib_nums(n):
#     for i in range(1, n+1):
#         print(trib_rec(i), "", end="")

number = input()

result = sorted(number)
result.reverse()
result = "".join([str(i) for i in result])

print(result)


# num = input()
#
# arr_digits = []
#
#
# def max_num(digits):
#     digits.sort(reverse=True)
#     number = ''.join(digits)
#
#     return number
#
#
# for digit in range(len(num)):
#     arr_digits.append(num[digit])
#
# print(max_num(arr_digits))

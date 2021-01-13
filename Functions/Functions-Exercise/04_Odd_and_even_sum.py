# def odd_even_sum(num):
#     odds = "".split()
#     evens = "".split()
#
#     for i in num:
#         if int(i) % 2 == 0:
#             evens += i
#         else:
#             odds += i
#     odds = [int(i) for i in odds]
#     evens = [int(i) for i in evens]
#
#
# number = input()
# print(f"Odd sum = {sum(odds)}, Even sum = {sum(evens)}")


def odd_even_sum(num):
    odds = sum([])
    evens = sum([])

    for i in num:
        if int(i) % 2 == 0:
            evens += int(i)
        else:
            odds += int(i)

    print(f"Odd sum = {odds}, Even sum = {evens}")


number = input()

odd_even_sum(number)

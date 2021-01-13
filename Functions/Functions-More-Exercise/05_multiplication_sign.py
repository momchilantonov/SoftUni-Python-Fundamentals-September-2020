num1 = int(input())
num2 = int(input())
num3 = int(input())


def sign_check(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    elif (n1 > 0 and n2 > 0 and n3 > 0) or (n1 > 0 and n2 < 0 and n3 < 0) \
            or (n1 < 0 and n2 > 0 and n3 < 0) or (n1 < 0 and n2 < 0 and n3 > 0):
        return "positive"
    else:
        return "negative"


print(f"{sign_check(num1, num2, num3)}")

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
#
# def m_sign(num1, num2, num3):
#     numbers = [num1, num2, num3]
#     pos_cnt = 0
#     neg_cnt = 0
#
#     for i in range(len(numbers)):
#         if numbers[i] > 0:
#             pos_cnt += 1
#         elif numbers[i] < 0:
#             neg_cnt += 1
#
#     if num1 == 0 or num2 == 0 or num3 == 0:
#         return "zero"
#     elif pos_cnt == 3 or (pos_cnt == 1 and neg_cnt == 2):
#         return "positive"
#     else:
#         return "negative"
#
#
# print(m_sign(n1, n2, n3))

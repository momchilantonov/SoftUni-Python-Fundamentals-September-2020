def palindrome(num):
    rev_num = num[::-1]
    if num == rev_num:
        return True
    else:
        return False


number = input().split(", ")
num = ''
for i in number:
    num = i
    print(palindrome(num))


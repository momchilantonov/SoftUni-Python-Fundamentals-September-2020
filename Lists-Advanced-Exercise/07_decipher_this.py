secret_message = input().split()

for word in secret_message:
    result = []
    numbers_in_message = [i for i in word if i.isdigit()]
    numbers_as_ascii = chr(int("".join(numbers_in_message)))
    result += numbers_as_ascii
    letters_in_message = [i for i in word if i.isalpha()]
    result += letters_in_message
    result[1], result[-1] = result[-1], result[1]
    print("".join(result), end=" ")

alphabet_dict = {chr(el+97): el+1 for el in range(26)}

line = input().split()

total_sum = 0

for ch in line:
    first_letter = ch[0]
    last_letter = ch[-1]
    number = int(ch[1:-1])

    if first_letter.isupper():
        number /= alphabet_dict[first_letter.lower()]
    elif first_letter.islower():
        number *= alphabet_dict[first_letter]

    if last_letter.isupper():
        number -= alphabet_dict[last_letter.lower()]
    elif last_letter.islower():
        number += alphabet_dict[last_letter]

    total_sum += number

print(f"{total_sum:.2f}")

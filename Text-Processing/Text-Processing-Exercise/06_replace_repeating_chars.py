text = input()
text_list = []

for letter in range(0, len(text)-1):
    if not text[letter] == text[letter+1]:
        text_list.append(text[letter])

text_list.append(text[-1])

print(f"{''.join(text_list)}")

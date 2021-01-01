chars = input()
chars_list = {}

for ch in "".join(chars.split()):
    chars_list[ch] = chars.count(ch)

for key, val in chars_list.items():
    print(f"{key} -> {val}")

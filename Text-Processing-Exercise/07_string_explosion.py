# text = input()
# field = text
# bomb = 0
# count = 0
#
# for el in range(len(text)):
#     if text[el] == ">":
#         count += 1
#     if bomb > 0 and text[el].isdigit():
#         field = field.replace(text[el], "", 1)
#         bomb -= 1
#     elif text[el] == ">":
#         bomb += int(text[el+1])
#
# [const, change] = field.split(">"*count)
#
# while bomb > 0:
#     for ch in range(len(change)):
#         change = change.replace(change[ch], "", 1)
# a=5

line = input()
strength = 0
new_string = ""
exploding = False
for k in range(len(line)):
    if line[k] == ">":
        if line[k+1].isdigit():
            strength += int(line[k+1])
        exploding = True
        new_string += line[k]
    elif exploding:
        if line[k] == ">":
            new_string += line[k]
            if line[k+1].isdigit():
                strength += int(line[k+1])
        else:
            strength -= 1
            if strength == 0:
                exploding = False
    else:
        new_string += line[k]
print(new_string)

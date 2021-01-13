import re

txt = input()

first_match = []
second_match = []
mirror_words = []

pattern = r"(?P<FB>[@#])(?P<match1>[A-Za-z]{3,})(?P=FB){2}(?P<match2>[A-Za-z]{3,})(?P=FB)"
# pattern = r"(?<=(?P<FB>[@#]))(?P<match1>[A-Za-z]{3,})(?P=FB){2}(?P<match2>[A-Za-z]{3,})(?=(?P=FB))"


pairs = re.finditer(pattern, txt)

for pair in pairs:
    first_match.append(pair["match1"])
    second_match.append(pair["match2"])

if len(first_match) == 0:
    print("No word pairs found!")
else:
    print(f"{len(first_match)} word pairs found!")

for el in range(len(first_match)):
    if first_match[el] == second_match[el][::-1]:
        mirror_words.append(first_match[el]+" <=> "+second_match[el])

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(f"{', '.join(mirror_words)}")

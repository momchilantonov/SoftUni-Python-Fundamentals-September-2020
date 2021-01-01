words = [word.lower() for word in input().split(" ")]
words_dict = {}

for w in words:
    words_dict[w] = words.count(w)

for key, val in words_dict.items():
    if val % 2 == 1:
        print(key, end=" ")

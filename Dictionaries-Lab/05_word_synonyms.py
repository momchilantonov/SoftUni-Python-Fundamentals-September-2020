target_count = int(input())
synonyms = {}

for _ in range(target_count):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = [synonym]
    else:
        synonyms[word].append(synonym)

for key, val in synonyms.items():
    print(f"{key} - {', '.join(val)}")

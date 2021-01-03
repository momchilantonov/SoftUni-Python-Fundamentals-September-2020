text = input()

emoticons = [text[ch+1] for ch in range(len(text)) if text[ch] == ":"]

for el in emoticons:
    print(f":{el}")

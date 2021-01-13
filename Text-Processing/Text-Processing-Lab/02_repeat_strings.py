words = input().split(" ")
result = ""
for word in words:
    result += word*len(word)

print(result)

words = input()

result = [index for index in range(len(words)) if words[index].isupper()]

print(result)

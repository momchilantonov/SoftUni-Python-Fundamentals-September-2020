import re

txt = input()
word = input()

pattern = fr"(?i)\b{word}\b"

result = re.findall(pattern, txt)

print(len(result))

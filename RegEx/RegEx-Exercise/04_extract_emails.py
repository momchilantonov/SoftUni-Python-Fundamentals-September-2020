import re

txt = input()

pattern = r"(^|(?<=\s))(?P<user>[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]+)@" \
          r"(?P<host>[a-zA-Z0-9]+[-]?[a-zA-Z0-9]+\.[a-zA-Z\.]{2,}\b)"

mails = re.finditer(pattern, txt)

for mail in mails:
    print(f"{mail['user']}@{mail['host']}")

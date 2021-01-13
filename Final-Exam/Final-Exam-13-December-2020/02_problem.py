import re

num_lines = int(input())

for line in range(num_lines):
    line_for_check = input()

    pattern = r"(?P<lb>[*|@]{1})(?P<tag>[A-Z]{1}[a-z]{2,})(?P=lb): " \
              r"\[(?P<letter1>[a-zA-Z]{1})\]\|\[(?P<letter2>[a-zA-Z]{1})\]\|\[(?P<letter3>[a-zA-Z]{1})\]\|?$"

    matches = re.search(pattern, line_for_check)

    if not matches:
        print("Valid message not found!")

    else:
        valid_lines = matches.groupdict()
        valid_lines["letter1"] = ord(valid_lines["letter1"])
        valid_lines["letter2"] = ord(valid_lines["letter2"])
        valid_lines["letter3"] = ord(valid_lines["letter3"])
        print(f"{valid_lines['tag']}: {valid_lines['letter1']} {valid_lines['letter2']} {valid_lines['letter3']}")

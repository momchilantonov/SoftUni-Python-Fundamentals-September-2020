import re

txt = input()
links = []

while txt:
    # pattern = r"(?P<first_check>^|(?<=\s))(?P<subdomain>www\.\b)(?P<domain>[a-zA-Z0-9\-]+\b)" \
    #           r"(?P<extension>\.[a-z]{1,})+(?P<last_check>$|(?=\s))"

    pattern = r"(?P<first_check>^|(?<=\s))(?P<subdomain>www\.\b)(?P<domain>[a-zA-Z0-9\-]+\b)(?P<extension>\.[a-z]{1,})+"

    valid_links = re.finditer(pattern, txt)

    for link in valid_links:
        links.append(link.group())

    txt = input()

print(*links, sep="\n")

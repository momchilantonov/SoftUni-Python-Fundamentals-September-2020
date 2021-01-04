import re

variables = input()

pattern = r"(?<!_.)(?<=_)(?P<result>[a-zA-Z\d]+\b)"

valid_variables = re.finditer(pattern, variables)

result = [var.group() for var in valid_variables]

print(f"{','.join(result)}")

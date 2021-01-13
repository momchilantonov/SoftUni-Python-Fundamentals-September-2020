user_names = input().split(", ")
result = []

for user in user_names:
    is_valid = True
    if 3 <= len(user) <= 16 and " " not in user:
        for ch in user:
            if not (ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_"):
                is_valid = False
                if not is_valid:
                    break
        if is_valid:
            result.append(user)

for user_name in result:
    print(f"{user_name}")

username = input()


def case(user, inst):
    if inst == "lower":
        user = user.lower()
    elif inst == "upper":
        user = user.upper()
    print(user)
    return user


def reverse(user, start, end, sub):
    sub = sub[::-1]
    if 0 <= start < len(user) > end > 0:
        print(sub)


def cut(user, sub):
    if sub not in username:
        print(f"The word {user} doesn't contain {sub}.")
        return user
    else:
        user = user.replace(sub, "", 1)
        print(user)
        return user


def replace(user, ch):
    user = user.replace(ch, "*")
    print(user)
    return user


def check(user, ch):
    if ch in user:
        print("Valid")
    else:
        print(f"Your username must contain {ch}.")


while True:
    command = input()
    if command == "Sign up":
        break

    actions = command.split(" ")
    action = actions[0]

    if action == "Case":
        case_action = actions[1]
        username = case(username, case_action)
    elif action == "Reverse":
        start_index = int(actions[1])
        end_index = int(actions[2])
        substring = username[start_index:end_index+1]
        reverse(username, start_index, end_index, substring)
    elif action == "Cut":
        substring = actions[1]
        username = cut(username, substring)
    elif action == "Replace":
        char = actions[1]
        username = replace(username, char)
    elif action == "Check":
        char = actions[1]
        check(username, char)

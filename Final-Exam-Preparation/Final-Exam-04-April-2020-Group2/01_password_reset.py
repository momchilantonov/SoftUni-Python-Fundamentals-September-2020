password = input()


def take_odd_action(old_pass):
    new_pass = ""
    for i in range(len(old_pass)):
        if i % 2 == 1:
            new_pass += old_pass[i]
    return new_pass


def cut_action(old_pass, cut_index, length_index):
    cut_chars = old_pass[cut_index:cut_index+length_index]
    new_pass = old_pass.replace(cut_chars, "", 1)
    return new_pass


def substitute_action(old_pass, old_char, new_char):
    if old_char in old_pass:
        new_pass = old_pass.replace(old_char, new_char)
        return new_pass


while True:
    command = input()
    if command == "Done":
        break

    txt = command.split(" ")

    if txt[0] == "TakeOdd":
        password = take_odd_action(password)
        print(password)
    elif txt[0] == "Cut":
        index = int(txt[1])
        length = int(txt[2])
        password = cut_action(password, index, length)
        print(password)
    elif txt[0] == "Substitute":
        substring = txt[1]
        substitute = txt[2]
        if substring in password:
            password = substitute_action(password, substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")

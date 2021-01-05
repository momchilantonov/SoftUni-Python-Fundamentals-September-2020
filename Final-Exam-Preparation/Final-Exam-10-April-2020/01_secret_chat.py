concealed_message = input()


def insert_space(message, index):
    first_part = message[:index]
    second_part = message[index:]
    new_message = first_part+" "+second_part
    print(new_message)
    return new_message


def reverse(message, substring):
    if substring in message:
        cut_message = message.replace(substring, "", 1)
        rev_substring = substring[::-1]
        new_message = cut_message+rev_substring
        print(new_message)
        return new_message
    else:
        print("error")
        return message


def change_all(message, substring, replacement):
    if substring in message:
        new_message = message.replace(substring, replacement)
        print(new_message)
        return new_message


while True:
    command = input()
    if command == "Reveal":
        break

    operations = command.split(":|:")

    if operations[0] == "InsertSpace":
        index = int(operations[1])
        concealed_message = insert_space(concealed_message, index)
    elif operations[0] == "Reverse":
        rev_substring = operations[1]
        concealed_message = reverse(concealed_message, rev_substring)
    elif operations[0] == "ChangeAll":
        change_substring = operations[1]
        replacement = operations[2]
        concealed_message = change_all(concealed_message, change_substring, replacement)

print(f"You have a new text message: {concealed_message}")

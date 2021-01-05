encrypted_msg = input()


def move(msg, num_ch):
    moved_msg, left_msg = msg[:num_ch], msg[num_ch:]
    result = left_msg+moved_msg
    return result


def insert(msg, i, val):
    msg_before, msg_after = msg[:i], msg[i:]
    result = msg_before+val+msg_after
    return result


def change_all(msg, sub_s, text):
    result = msg.replace(sub_s, text)
    return result


while True:
    instruction = input()
    if instruction == "Decode":
        break

    operations = instruction.split("|")
    curr_operation = operations[0]

    if curr_operation == "Move":
        num_chars = int(operations[1])
        encrypted_msg = move(encrypted_msg, num_chars)
    elif curr_operation == "Insert":
        index = int(operations[1])
        value = operations[2]
        encrypted_msg = insert(encrypted_msg, index, value)
    elif curr_operation == "ChangeAll":
        substring = operations[1]
        replacement_text = operations[2]
        encrypted_msg = change_all(encrypted_msg, substring, replacement_text)

print(f"The decrypted message is: {encrypted_msg}")

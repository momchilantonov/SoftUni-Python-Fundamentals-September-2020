
def repeat_string(repeat_text, repeat_time):
    result = ""
    for _ in range(repeat_time):
        result += repeat_text
    return result


text = input()
repeats_qty = int(input())

print(repeat_string(text, repeats_qty))

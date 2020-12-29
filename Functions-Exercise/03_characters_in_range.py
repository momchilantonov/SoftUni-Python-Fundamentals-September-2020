def ascii_table(char_1, char_2):
    string_result = ""

    for i in range(char_1+1, char_2):
        string_result += chr(i)

    result = " ".join(string_result)

    return result


character_1 = ord(input())
character_2 = ord(input())

print(ascii_table(character_1, character_2))

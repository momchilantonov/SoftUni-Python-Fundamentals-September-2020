def in_list(word):
    test_list = ["coding", "dog", "cat", "movie"]
    if word.lower() in test_list:
        return True
    return False


coffee_counter = 0

while True:
    command = input()
    if command == "END":
        break

    if in_list(command) and command.islower():
        coffee_counter += 1
    elif in_list(command) and command.isupper():
        coffee_counter += 2

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)


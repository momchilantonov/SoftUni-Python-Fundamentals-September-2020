def password_validation(password):
    sum_chars = 0
    sum_digits = 0
    sum_special_char = 0
    is_valid = True
    for index in range(len(password)):
        sum_chars += 1
        if password[index].isdigit():
            sum_digits += 1
        if not password[index].isalpha() and not password[index].isdigit():
            sum_special_char += 1
    if not 6 <= sum_chars <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not sum_special_char == 0:
        is_valid = False
        print("Password must consist only of letters and digits")
    if sum_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


password_for_check = input()
password_for_check = [password_for_check[char] for char in range(len(password_for_check))]

password_validation(password_for_check)

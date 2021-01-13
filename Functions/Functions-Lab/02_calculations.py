def calculations(operator, first_num, second_num):
    result = None
    if operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num // second_num
    elif operator == 'add':
        result = first_num+second_num
    elif operator == 'subtract':
        result = first_num-second_num
    return result


operation = input()
num_1 = int(input())
num_2 = int(input())

print(calculations(operation, num_1, num_2))

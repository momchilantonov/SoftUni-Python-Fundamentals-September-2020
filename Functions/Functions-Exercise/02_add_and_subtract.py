def add_sub(num_1, num_2, num_3):
    def add(num_1, num_2):
        result = num_1+num_2
        return result

    def sub():
        return add(num_1, num_2)-num_3

    return sub()


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_sub(number_1, number_2, number_3))

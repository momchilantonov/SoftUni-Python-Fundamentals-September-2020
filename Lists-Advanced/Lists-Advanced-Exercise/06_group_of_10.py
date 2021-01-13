list_of_numbers = [int(i) for i in input().split(", ")]

boundary_value = 10


def empty_list(checked_list):
    if not checked_list:
        return True
    return False


while not empty_list(list_of_numbers):
    result = [i for i in list_of_numbers if i <= boundary_value]
    list_of_numbers = [i for i in list_of_numbers if i not in result]
    print(f"Group of {boundary_value}'s: {result}")
    boundary_value += 10

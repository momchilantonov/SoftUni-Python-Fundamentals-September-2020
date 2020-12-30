list_of_numbers = input()
list_of_numbers_int = [int(element) for element in list_of_numbers.split(", ")]

indices_of_evens = [index for index in range(len(list_of_numbers_int)) if list_of_numbers_int[index] % 2 == 0]

print(indices_of_evens)

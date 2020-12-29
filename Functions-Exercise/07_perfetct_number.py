def perfect_number(number):
    sum_indexes = 0
    for index in range(1, (number // 2)+1):
        if number % index == 0:
            sum_indexes += index
    return sum_indexes


num = (input())

if perfect_number(num) == num:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


def exchange(numbers, i):
    if 0 <= i < len(numbers):
        first_list = numbers[:i+1]
        second_list = numbers[i+1:]
        result = second_list+first_list
        return result
    print("Invalid index")
    return numbers


def max_even_odd(numbers, num_type):
    if num_type == "even":
        even_list = [i for i in numbers if i % 2 == 0]
        if not even_list:
            return "No matches"
        else:
            max_even = max(even_list)
            for i in range(len(numbers)-1, -1, -1):
                if numbers[i] == max_even:
                    return i
    elif num_type == "odd":
        odd_list = [i for i in numbers if i % 2 == 1]
        if not odd_list:
            return "No matches"
        else:
            max_odd = max(odd_list)
            for i in range(len(numbers)-1, -1, -1):
                if numbers[i] == max_odd:
                    return i


def min_even_odd(numbers, num_type):
    if num_type == "even":
        even_list = [i for i in numbers if i % 2 == 0]
        if not even_list:
            return "No matches"
        else:
            min_even = min(even_list)
            for i in range(len(numbers)-1, -1, -1):
                if numbers[i] == min_even:
                    return i
    elif num_type == "odd":
        odd_list = [i for i in numbers if i % 2 == 1]
        if not odd_list:
            return "No matches"
        else:
            min_odd = min(odd_list)
            for i in range(len(numbers)-1, -1, -1):
                if numbers[i] == min_odd:
                    return i


def first_even_odd(numbers, counter, num_type):
    if num_type == "even":
        evens_count = int(counter)
        first_evens = [i for i in numbers if i % 2 == 0]
        if evens_count <= len(numbers):
            result = [i for i in first_evens[:evens_count] if i % 2 == 0]
            return result
        return "Invalid count"
    elif num_type == "odd":
        odds_count = int(counter)
        first_odds = [i for i in numbers if i % 2 == 1]
        if odds_count <= len(numbers):
            result = [i for i in first_odds[:odds_count] if i % 2 == 1]
            return result
        return "Invalid count"


def last_even_odd(numbers, counter, num_type):
    if num_type == "even":
        evens_count = int(counter)
        last_evens = [i for i in numbers if i % 2 == 0]
        if evens_count <= len(numbers):
            result = [i for i in last_evens[evens_count::-1] if i % 2 == 0]
            return result
        return "Invalid count"
    elif num_type == "odd":
        odds_count = int(counter)
        last_odds = [i for i in numbers if i % 2 == 1]
        if odds_count <= len(numbers):
            result = [i for i in last_odds[odds_count::-1] if i % 2 == 1]
            return result
        return "Invalid count"


array = [int(i) for i in input().split()]

command = input()

while not command == "end":
    data = command.split()
    if data[0] == "exchange":
        array = exchange(array, int(data[1]))
    elif data[0] == "max":
        print(max_even_odd(array, data[1]))
    elif data[0] == "min":
        print(min_even_odd(array, data[1]))
    elif data[0] == "first":
        print(first_even_odd(array, int(data[1]), data[2]))
    elif data[0] == "last":
        print(last_even_odd(array, int(data[1]), data[2]))

    command = input()

print(array)

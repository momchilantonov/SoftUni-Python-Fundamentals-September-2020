list_of_strings_1 = input().split(", ")
list_of_strings_2 = input().split(", ")

new_string = [i for i in list_of_strings_1 for el in list_of_strings_2 if i in el]

print(sorted(set(new_string), key=new_string.index))


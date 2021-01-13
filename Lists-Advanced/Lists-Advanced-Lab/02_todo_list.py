notes = input()

priorities_list = ["*" for i in range(10)]

while notes != "End":
    notes_data = notes.split("-")
    priority = int(notes_data[0])
    note = notes_data[1]
    priorities_list.insert(priority, note)
    priorities_list.remove("*")
    notes = input()

result = [note for note in priorities_list if note != "*"]

print(result)

# command = input()
# todo_list = [0] * 10
# while not command == "End":
#     importance, value = command.split("-")
#     importance = int(importance)
#     todo_list.insert(importance, value)
#     todo_list.remove(0)
#
#     command = input()
#
# list_importance = list(values for values in todo_list if not values == 0)
#
# print(list_importance)
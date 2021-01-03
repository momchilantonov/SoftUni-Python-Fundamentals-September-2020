path = input().split("\\")

for el in path:
    if "." in el:
        [file_name, file_extension] = el.split(".")

        print(f"File name: {file_name}")
        print(f"File extension: {file_extension}")
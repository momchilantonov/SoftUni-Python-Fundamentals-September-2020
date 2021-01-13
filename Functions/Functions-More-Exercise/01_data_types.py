data_type = input()
data_input = input()


def data_types(type, data):
    if type == "int":
        data = int(data) * 2
    elif type == "real":
        data = f"{float(data) * 1.5:.2f}"
    elif type == "string":
        data = f"${data}$"
    print(data)


data_types(data_type, data_input)

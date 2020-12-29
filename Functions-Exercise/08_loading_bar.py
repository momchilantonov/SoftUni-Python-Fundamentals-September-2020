number = int(input()) // 10

loading_bar = ["." for _ in range(10)]


def loading(num):
    for i in range(num):
        loading_bar.insert(i, "%")
        loading_bar.pop()
    return loading_bar


loading(number)

if "." not in loading_bar:
    print("100% Complete!")
    print(f"[{''.join(loading_bar)}]")
else:
    print(f"{number * 10}% [{''.join(loading_bar)}]")
    print("Still loading...")

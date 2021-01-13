current_version = int("".join([i for i in input().split(".")]))

new_version = ".".join(str(current_version+1))

print(new_version)

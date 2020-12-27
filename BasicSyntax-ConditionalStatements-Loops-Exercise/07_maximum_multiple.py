divisor = int(input())
bound = int(input())

highest_divisor = 0

for i in range(0, bound+1):
    if i % divisor == 0:
        highest_divisor = i

print(highest_divisor)

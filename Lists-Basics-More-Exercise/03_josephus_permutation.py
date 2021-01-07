circle = input().split(' ')
kill_count = int(input())
result = []
counter = 0

index = 0
while len(circle) > 0:
    counter += 1

    if counter % kill_count == 0:
        result.append(circle.pop(index))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))


# def josephus(n, k):
#     if n == 1:
#         return 1
#     else:
#         return (josephus(n-1, k)+k-1) % n+1
#
#
# print(josephus(len(people), kth))

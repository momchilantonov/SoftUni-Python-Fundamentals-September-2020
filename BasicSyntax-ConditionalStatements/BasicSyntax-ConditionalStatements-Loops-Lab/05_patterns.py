num = int(input())

for row_pos in range(1, num+1):
    print('*' * row_pos)

for row_neg in range(num-1, 0, -1):
    print('*' * row_neg)

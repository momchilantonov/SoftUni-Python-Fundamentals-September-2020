n = int(input())

for i in range(n):
    for k in range(n):
        for j in range(n):
            print(f'{chr(97+i)}{chr(97+k)}{chr(97+j)}')

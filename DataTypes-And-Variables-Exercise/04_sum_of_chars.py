num_chars = int(input())

result = 0

for i in range(num_chars):
    letter = input()
    result += ord(letter)

print(f'The sum equals: {result}')

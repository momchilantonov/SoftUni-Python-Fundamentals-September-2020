key = int(input())
lanes = int(input())

message = []

for symbol in range(lanes):
    letter = input()
    decrypt_letter = ord(letter)+key
    message.append(chr(decrypt_letter))

print(f"{''.join(message)}")

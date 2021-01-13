text = input()
encrypted_text = []

for ch in text:
    encrypted_text.append(ord(ch)+3)

print(f"{''.join([chr(i) for i in encrypted_text])}")

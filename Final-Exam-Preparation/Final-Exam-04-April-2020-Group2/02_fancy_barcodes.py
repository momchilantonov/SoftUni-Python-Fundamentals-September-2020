import re

pattern = r"(?P<first_symbol>@#{1,})(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<last_symbol>@#{1,})"

barcodes_count = int(input())

for _ in range(barcodes_count):
    barcode = input()
    digits = ""
    is_valid = re.match(pattern, barcode)
    if is_valid:
        valid_barcode = is_valid.groupdict()
        for ch in valid_barcode["barcode"]:
            if ch.isdigit():
                digits += ch
        if len(digits) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")

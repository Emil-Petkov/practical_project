n_symbols = int(input())

sum = 0

for iteration in range(n_symbols):
    symbol_from_ascii = input()
    convert = ord(symbol_from_ascii)
    sum += int(convert)

print(f"The sum equals: {sum}")

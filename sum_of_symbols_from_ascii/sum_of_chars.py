n_symbols = int(input())

sum_score = 0

for iteration in range(n_symbols):
    symbol_of_ascii = input()
    convert = ord(symbol_of_ascii)
    sum_score += int(convert)

print(f"The sum equals: {sum_score}")

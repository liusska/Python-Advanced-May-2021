data = input()

symbols = {}

for ch in data:
    if ch not in symbols:
        symbols[ch] = 0
    symbols[ch] += 1

sorted_symbols = sorted(symbols.items(), key=lambda x: x[0])

for key, value in sorted_symbols:
    print(f'{key}: {value} time/s')
numbers = input()

reversed_numbers = [el for x in numbers.split("|")[::-1] for el in x.split(" ") if el != ""]

print(' '.join(reversed_numbers))
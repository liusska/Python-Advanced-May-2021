# file = open("numbers.txt")
# result = 0
# for number in file:
#     result += int(number)
# file.close()
# print(result)

print(sum([int(x) for x in open("numbers.txt")]))

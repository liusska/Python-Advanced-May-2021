numbers_dictionary = {}

line = input()
while not line == "Search":
    try:
        numbers_dictionary[line] = int(input())
    except ValueError:
        print("The variable number must be an integer")
    line = input()


searched_number = input()
while not searched_number == "Remove":
    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")
    searched_number = input()


number_to_remove = input()
while not number_to_remove == "End":
    try:
        del numbers_dictionary[number_to_remove]
    except KeyError:
        print("Number does not exist in dictionary")
    number_to_remove = input()

print(numbers_dictionary)
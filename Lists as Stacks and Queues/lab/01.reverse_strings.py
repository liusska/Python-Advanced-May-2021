data = input()
data_as_list = [ch for ch in data]

reversed_data = ''
while data_as_list:
    reversed_data += data_as_list.pop()

print(reversed_data)
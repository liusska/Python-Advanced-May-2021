expression = input()

index_list = []
subexpression = []
for i in range(len(expression)):
    if expression[i] == '(':
        index_list.append(i)
    elif expression[i] == ')':
        start_idx = index_list.pop()
        subexpression.append(expression[start_idx: i+1])
        print(''.join(subexpression))
        subexpression = []

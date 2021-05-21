data = input()
parentheses = []
balanced = True

for ch in data:
    if ch == "[" or ch == "{" or ch == "(":
        parentheses.append(ch)
    elif ch == "]" or ch == "}" or ch == ")":
        if len(parentheses) == 0:
            balanced = False
            break
        el = parentheses.pop()
        if el == "[" and ch == "]":
            balanced = True
        elif el == "{" and ch == "}":
            balanced = True
        elif el == "(" and ch == ")":
            balanced = True
        else:
            balanced = False
            break


if balanced:
    print("YES")
else:
    print("NO")

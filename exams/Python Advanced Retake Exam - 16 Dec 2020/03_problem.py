def get_magic_triangle(n):
    triangle = []
    if n == 1:
        triangle.append([1])
    elif n == 2:
        triangle.append([1])
        triangle.append([1, 1])
    else:
        triangle = [[1], [1, 1]]
        while len(triangle) < n:
            current_row = triangle[len(triangle) - 1]
            new_row = [1]
            for i in range(len(triangle)):
                if i == len(current_row) - 1:
                    pass
                else:
                    new_row.append((current_row[i] + current_row[i + 1]))
            new_row.append(1)
            triangle.append(new_row)
    return triangle


print(get_magic_triangle(5))

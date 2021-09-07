from collections import deque


def fill_the_box(h, l, w, *args):
    args = deque(args)
    space = h * l * w
    cubes_to_fill = 0
    while args:
        cube = args.popleft()
        if cube == "Finish":
            if cubes_to_fill < space:
                return f"There is free space in the box. You could put {abs(space - cubes_to_fill)} more cubes."
        cubes_to_fill += cube
        if cubes_to_fill > space:
            diff = abs(space - cubes_to_fill)
            args.appendleft(diff)
            args.pop()
            return f"No more free space! You have {sum(args)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
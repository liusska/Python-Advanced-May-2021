from collections import deque


def math_operations(*args, **kwargs):
    args = deque(int(x) for x in args)
    while args:
        if args:
            kwargs['a'] += args.popleft()
        if args:
            kwargs['s'] -= args.popleft()
        if args:
            valid_el = args.popleft()
            if not valid_el == 0:
                kwargs['d'] /= valid_el
        if args:
            kwargs['m'] *= args.popleft()

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
# print(math_operations(6, a=0, s=0, d=0, m=0))
n, m = input().split()
n = int(n)
m = int(m)

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

intersection_set = n_set.intersection(m_set)
[print(x) for x in intersection_set]
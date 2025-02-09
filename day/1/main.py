from functools import reduce
from operator import add

A, B = [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]

with open("input.txt", 'r') as f:
    lines = list(map(lambda x: x.strip('\n').split(), f.readlines()))
    A, B = list(), list()
    for i in range(0, len(lines)):
        A.append(int(lines[i][0]))
        B.append(int(lines[i][1]))

A = sorted(A)
B = sorted(B)

diff = lambda a, b: a - b if a > b else b - a
for i in range(0, max(len(A), len(B))):
    A[i] = diff(A[i], B[i])

print(reduce(add, A))


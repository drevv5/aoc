from operator import sub
from math import fabs

def is_safe(A, i=1):
    r = lambda x: fabs(x) in range(1, 4)
    R = lambda x, y, z: r(sub(x, y)) and r(sub(y, z))
    t = lambda x, y, z: x < y < z or x > y > z

    Ai = (A[i-1], A[i], A[i+1])
    try:
        if R(*Ai) and t(*Ai):
            return is_safe(A, i+1)
        else:
            print("echo")
    except IndexError:
        return True if i == len(A)-2 and t(*Ai) else False


A = [[60, 61, 62, 60, 64]]

with open("input.txt", 'r') as f:
    A = list(map(lambda x: x.strip('\n').split(), f.readlines()))

c = 0
for a in A:
    a = tuple(map(int, a))
    print(a)
    if is_safe(a):
        c+=1

print(c)

import math

N = int(input())
A = [int(a) for a in input().split() if a != '0']

print(math.ceil(sum(A) / len(A)))

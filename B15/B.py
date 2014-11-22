import math

N = int(input())
A = map(int, input().split())

an = [an for an in A if an > 0]

print(math.ceil(sum(an) / len(an)))

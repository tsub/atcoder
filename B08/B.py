from collections import Counter

n = input()
sn = []

for i in range(n):
    sn.append(raw_input())

print Counter(sn).most_common(1)[0][0]

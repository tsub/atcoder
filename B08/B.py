from collections import Counter

n = int(raw_input())
sn = []

for i in range(n):
    sn.append(raw_input())

print Counter(sn).most_common()[0][0]

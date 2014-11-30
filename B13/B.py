A = int(raw_input())
B = int(raw_input())

l = [A, B]

if (max(l) - min(l)) >= 5:
    print 10 - max(l) + min(l)
else:
    print max(l) - min(l)

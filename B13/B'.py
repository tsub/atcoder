l = [int(raw_input()), int(raw_input())]
print 10 - max(l) + min(l) if max(l) - min(l) >= 5 else max(l) - min(l)
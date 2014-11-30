alphabets = ["A", "B", "C", "D", "E"]

input = raw_input()

for i in range(len(alphabets)):
    if alphabets[i] == input:
        print i + 1

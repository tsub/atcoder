N, H = raw_input().split()
A, B, C, D, E = raw_input().split()
expences = 0

N = int(N)
H = int(H)
A = int(A)
B = int(B)
C = int(C)
D = int(D)
E = int(E)

while N > 0:
  if H > E:
    H -= E

  elif N == 1:
    H += D
    expences += C

  elif D + H > E:
    H += D
    expences += C

  elif B + H > E:
    H += B
    expences += A

  else:
    H += D
    expences += C

  N -= 1

print expences
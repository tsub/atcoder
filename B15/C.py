import itertools

N, K = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))

l = [[] for i in range(N-1)]
for i in range(N-1):
    for j in range(K):
        all_patern = list(itertools.combinations([T[i][j]] + T[i+1], 2))
        for k in all_patern:
            if k[0] == T[i][j]:
                l[i].append(k)

aaa = []
for i in range(len(l)):
    print(l[i])
    for j in range(len(l[i])):
        for k in l[i][j]:
            aaa.append(k)
        aaa.append(l[i+1][j][1])
        # if len(set(aaa)) == 3:
        print(aaa)
        aaa.clear()

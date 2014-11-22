R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
data = [input() for i in range(R)]

node_map = [[i, j] for i in range(len(data)) for j in range(len(data[i])) if data[i][j] == '.']

map_lst = [[False for j in range(len(node_map))] for i in range(len(node_map))]

for i in range(len(node_map)):
    x, y = node_map[i][0], node_map[i][1]
    for xy in [[x, y+1], [x+1, y], [x-1, y], [x, y-1]]:
        if xy in node_map:
            map_lst[i][node_map.index(xy)] = True

START = node_map.index([sx-1, sy-1])
GOAL = node_map.index([gy-1, gx-1])

from queue import Queue
q = Queue()
q.put([START, 0])
checked = []
while not q.empty():
    current_state, current_depth = q.get()

    if current_state in checked:
        continue

    if current_state == GOAL:
        print(current_depth)
        break

    current_depth += 1
    for next_state in range(len(node_map)):
        if map_lst[current_state][next_state]:
            q.put([next_state, current_depth])

    checked.append(current_state)

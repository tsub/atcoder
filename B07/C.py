R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
data = []
for i in range(R):
    data.append(input())

node_map = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '.':
            node_map.append([i, j])

print(node_map)

map_lst = [[False for j in range(len(node_map))] for i in range(len(node_map))]

for i in range(len(node_map)):
    if [node_map[i][0], node_map[i][1]+1] in node_map:
        map_lst[i].insert(node_map.index(
            [node_map[i][0], node_map[i][1]+1]
        ), True)

    if [node_map[i][0]+1, node_map[i][1]] in node_map:
        map_lst[i].insert(node_map.index(
            [node_map[i][0]+1, node_map[i][1]]
        ), True)

    if [node_map[i][0]-1, node_map[i][1]] in node_map:
        map_lst[i].insert(node_map.index(
            [node_map[i][0]-1, node_map[i][1]]
        ), True)

    if [node_map[i][0], node_map[i][1]-1] in node_map:
        map_lst[i].insert(node_map.index(
            [node_map[i][0], node_map[i][1]-1]
        ), True)

print(map_lst)

from queue import Queue
q = Queue()
q.put([node_map.index([sx-1, sy-1]), 0])
checked = []
while not q.empty():
    current_state, current_depth = q.get()

    if current_state in checked:
        continue

    print(current_state, current_depth)

    if [gx-1, gy-1] in node_map:
        if current_state == node_map.index([gx-1, gy-1]):
            print(current_depth)
            break

    current_depth += 1
    for next_state in range(len(node_map)):
        if map_lst[current_state][next_state]:
            q.put([next_state, current_depth])

    checked.append(current_state)

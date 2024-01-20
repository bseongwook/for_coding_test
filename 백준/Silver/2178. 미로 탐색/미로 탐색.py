from collections import deque

N, M = map(int, input().split())

map_ = []
for _ in range(N):
    map_.append(list(map(int, list( input() ))))

q = deque()
q.append((0,0,1))
map_[0][0] = 0 # 방문 처리

# 하우 상좌
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    cur_x, cur_y, num_of_moves = q.popleft()

    if cur_x == N-1 and cur_y == M-1:
        print(num_of_moves)
        break

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x <= N-1 and 0 <= next_y <= M-1 and map_[next_x][next_y] == 1:
            q.append((next_x, next_y, num_of_moves+1))
            map_[next_x][next_y] = 0


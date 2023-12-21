# 완전 탐색
# 섬들이 숫자로 이루어져있다고 가정, 대각선도 연결되어 있는지 확인

# m행, n열

# b, d 모두 풀이 가능
from collections import deque

def numIsland(grid):
    num_of_island = 0
    m = len(grid) # row
    n = len(grid[0]) # col
    visited = [[False]*n for _ in range(m)]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1] # 상하좌우

        visited[x][y] = True # 방문처리
        queue = deque((x, y))
        while queue: # 큐가 전부 소진될때까지
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if visited and 0 <= next_x <= m and 0 <= next_y <= n \
                    and not visited[next_x][next_y] and grid[next_x][next_y] == '1':
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
    return num_of_island
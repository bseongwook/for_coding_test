from collections import deque

N, M, V = map(int, input().split())

map_ = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    map_[n1][n2] = True
    map_[n2][n1] = True

dfs_visited = []
def dfs(row):
    dfs_visited.append(row)
    
    for idx in range(len(map_[row])):
        if map_[row][idx] and idx not in dfs_visited:
            dfs(idx)
dfs(V)

bfs_visited = []
q = deque()
q.append(V)
bfs_visited.append(V)
def bfs(row):
    while q:
        r = q.popleft()

        for idx in range(len(map_[r])):
            if map_[r][idx] and idx not in bfs_visited:
                q.append(idx)
                bfs_visited.append(idx)
bfs(V)

for e in dfs_visited:
    print(e, end =' ')
print()
for e in bfs_visited:
    print(e, end =' ')    
# 미로찾기 문제, 최단거리 문제 => bfs로 완전탐색 한다고 생각
# 목적지에 도달해서 처음으로 번호를 매기면 거기서 함수 종료

# 만약 dfs면 목적지에 도달하는 모든 경우의 수를 따져서 몇 번만에 가는지 비교

from collections import deque

def shorpath(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)] # grid와 같은 사이즈
    
    delta = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

    if grid[0][0] != 0 or grid[row-1][col-1] == 1: # 시작을 못하거나 도착을 못하면 바로 종료
        return shortest_path_len
    
    queue = deque() # 0,0의 길이정보는 1
    queue.append((0,0,1)) # 튜플은 deque선언과 동시에 초기화 불가능 (deque((0,0,1)) 못함)
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        
        if cur_r == row -1 and cur_c == col- 1: # 목적지에 도착했을 때
            shortest_path_len = cur_len
            break

        for i in range(8):
            for dr, dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if 0<=next_r<row and 0<=next_c<col and grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True

    return shortest_path_len
from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]: # 현재 노드와 인접한 노드 전부 방문
            if v not in visited:
                visited.append(v)
                queue.append(v)
    
    return visited
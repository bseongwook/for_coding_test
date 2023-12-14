# 그래프 표시 형식은 인접리스트(딕셔너리 사용)형식

visited = []
graph = {}

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs( v)
    return visited

# dfs(grpah, 'A')

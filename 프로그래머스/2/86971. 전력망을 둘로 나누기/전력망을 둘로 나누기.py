from collections import deque
  
def bfs(node, map_):
    visited = [node]
    c = 0
    q = deque()
    q.append(node)
    c += 1
    
    while q:
        current_node = q.popleft()
        
        for col in range(len(map_[current_node])):
            if map_[current_node][col] == 1 and col not in visited:
                q.append(col)
                visited.append(col)
                c += 1
    return c
    
def solution(n, wires):
    
    wires = deque(wires)
    map_ = [ [0]*n for _ in range(n) ]
    
    for wire in wires:
        map_[wire[0]-1][wire[1]-1] = 1
        map_[wire[1]-1][wire[0]-1] = 1
    answer = n
    
    for wire in wires: # 하나씩 제외
        
        map_[wire[0]-1][wire[1]-1] = 0
        map_[wire[1]-1][wire[0]-1] = 0
        
        connected_num1 = bfs(wire[0]-1, map_)
        connected_num2 = n - connected_num1
        
        if abs(connected_num1 - connected_num2) < answer:
            answer = abs(connected_num1 - connected_num2)
        
        map_[wire[0]-1][wire[1]-1] = 1
        map_[wire[1]-1][wire[0]-1] = 1
        
    return answer
    
    
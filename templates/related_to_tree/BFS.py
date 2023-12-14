from collections import deque

# 암기

def bfs(root):
    visited = []
    if root in None:
        return []
    q = deque() # 어디 방문할 지 예약 - 삽입, 삭제 모두 O(1)
    q.append(root)

    # 접근은 cur_node를 통해 하고, 방문은 visited에 담기 

    while q:
        cur_node = q.popleft() # O(1)
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

# 결과적으로 마지막 노드는 visited에 담기고 cur_node에 남아있는 상태

bfs(root)

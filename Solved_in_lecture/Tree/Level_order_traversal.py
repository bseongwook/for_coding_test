# maximum depth of binary tree
# tree 문제는 구현아니면 순회 (level, post order 위주로 생각)
# level order는 bfs와 거의 동일 - deque() 쓰고 시작

# 깊이 : root에서 얼마나 떨어져 있나 : 여기서는 시작이 1

# 큐 마지막에 방문한 노드의 dpeth가 정답

# 트리순회, 레벨오더순회 =  bfs 라고 생각
# bfs, dfs는 그래프에서 많이 쓰긴 함

# leetcode 104

from collections import deque

def maxDepth(root): # 노드를 저장할 떄 이 노드의 깊이를 같이 저장해야 됨
    max_depth = 0
    if root is None:
        return max_depth

    q = deque()
    q.append((root ,1)) # 오른 쪽은 depth 정보, root는 1로 설정

    while q: # q에 원소가 존재한다면
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))
    
    return max_depth

# 알고리즘 상으론 문제 없지만 입력으로 리스트가 들어온 경우 할 수 없음

class TreeNode:
    def __init__(self, l=None ,r=None, v=0) -> None:
        self.left = l
        self.right = r
        self.value = v

# 이런 식으로 class 구성해서 알고리즘 확인할 경우 사용

# 아래는 level order가 아닌 post order 방식으로 풀 수 있음
# 각 노드의 깊이 값(leaf노드라면 1)을 return 하고,
# 상위 노드는 아래의 깊이 값 중 큰 값에 1을 더해서 위로 return 한다.

def maxdepth(root):
    if cur_node is None:
        return 0  # depth
    
    left_depth = maxdepth(root.left)
    right_dept = maxdepth(root.right)
    return max(left_depth, right_dept) + 1



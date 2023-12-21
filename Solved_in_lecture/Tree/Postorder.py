# lowest common ancestor of a binary tree

# 조상 노드는 문제에 따라 정의 다름
# 여기서는 나 포함 위의 모든 노드

# 아래의 코드에서 하나의 노드도 작은 트리 취급

# 일종의 template으로 여기기

# postorder 순회 방식
def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == p or root == q: # 지나치는 노드가 문제에서 들어온 노드면 해당 노드가 조상
        return root
    elif left and right: # 한 노드 입장에서 양쪽의 자식 노드에서 접근하게 된다면 해당 노드가 조상
        return root
    
    return left or right 

LCA([3,5,1,6,2,0,8,None, None,7,4], 6, 4) # 완전 이진트리 형식으로 입력
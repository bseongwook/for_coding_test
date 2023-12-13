# DFS는 left_child, right_child 중 어떤 것부터 할지 작성하는 바에 따라 순서 달라짐

def dfs(cur_node):
    if cur_node in None:
        return
    
    dfs(cur_node.left)
    dfs(cur_node.right)


# 접근은 위와 같이, 방문은 언제 하는지에 따라 3가지 방법으로 나눔 (전위, 중위, 후위)

# 전위 순회 preorder
def preorder(cur_node):
    if cur_node is None:
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

# 중위 순회 
def inorder(cur_node):
    if cur_node is None:
        return
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

# 후위 순회 
def postorder(cur_node):
    if cur_node is None:
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)

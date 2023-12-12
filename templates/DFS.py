# DFS는 left_child, right_child 중 어떤 것부터 할지 작성하는 바에 따라 순서 달라짐

def dfs(cur_node):
    if cur_node in None:
        return
    
    dfs(cur_node.left)
    dfs(cur_node.right)

dfs(root)
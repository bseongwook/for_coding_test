class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value =2)
bt.root.right = Node(value =3)
bt.root.left.left = Node(value =4)
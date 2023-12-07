class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # 데이터 원소를 처음 만들 경우
            self.head = new_node
        else: # 원소가 하나 이상 있어서 이미 head가 원소를 가리키는 경우
            current = self.head
            while(current.next): # next node가 None이 될 때까지 실행 -- 직접 구현 가능 ???
                current = current.next
            current.next = new_node

    def get(self, idx):
        current = self.head
        for _ in range(idx): # 여러번 이동해야 되기 때문에 O(n), 근데 한 번에 할 수 있음
            current = current.next
        return current.value

    def insert_at(self, idx, value):
        new_node = Node(value)
        if self.head is None: # 원소가 하나도 없을 경우
            self.head = new_node
        else:
            pass

    def remove_at(self, idx):
        pass

    def insert_back(self, value): # tail을 써서 O(1)으로 구현
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 노드가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

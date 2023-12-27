from collections import deque

q = deque()

def push_front(x):
    q.appendleft(x)

def push_back(x):
    q.append(x)

def pop_front():
    return -1 if len(q) == 0 else q.popleft()

def pop_back():
    return -1 if len(q) == 0 else q.pop()

def size():
    return len(q)

def empty():
    return 0 if len(q) == 0 else 1

def front():
    print()

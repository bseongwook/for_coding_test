from collections import deque

def solution(priorities, location):
    
    answer = []
    # priorities는 각 자리인덱스(키)의 value라고 생각
    dic = {idx : p for idx, p in enumerate(priorities)} # {0: 2, 1: 1, 2: 3, 3: 2}
    
    # 인덱스로 배열 만들고 그걸로 조작
    lst = [i for i in range(len(priorities))]
    lst = deque(lst)
    
    while len(lst) > 0:
        
        if dic[lst[0]] == max(dic.values()): # max(priorities)업뎃 안됨
            temp = lst[0]
            answer.append(lst.popleft())
            del dic[temp]
        else:
            lst.rotate(-1)

    return answer.index(location) + 1
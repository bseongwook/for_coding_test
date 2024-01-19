from collections import deque
import sys
sys.setrecursionlimit(10**6)

# 이 문제를 처음 보고 어떻게 dp나 bfs로 풀 생각을 하는건가?
# dfs는 런타임 에러 발생해서 bfs로 풀이

def solution(x, y, n):

    q = deque()
    q.append((x, 0)) # 계산한 횟수 추가
    
    dic = {}
    
    while q:
        temp = q.popleft()
        # print(temp)
        cur_x = temp[0]
        calculate_cnt = temp[1]
        
        if cur_x == y:
            return calculate_cnt
        elif cur_x < y:
            if cur_x + n not in dic:
                q.append((cur_x + n, calculate_cnt+1))
                dic[cur_x + n] = False
            if cur_x * 2 not in dic:
                q.append((cur_x * 2, calculate_cnt+1))
                dic[cur_x * 2] = False
            if cur_x * 3 not in dic: 
                q.append((cur_x * 3, calculate_cnt+1))
                dic[cur_x * 3] = False
    
    return -1
        
    
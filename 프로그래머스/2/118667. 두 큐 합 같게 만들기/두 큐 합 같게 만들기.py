from collections import deque

def solution(queue1, queue2):
    
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 == 1: # 합이 홀수면 같게 못함
        return -1 
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # sum()을 매번 반복하면 시간이 너무 걸림
    # 한 번 sum을 계산한 다음, 변화량만 더하거나 빼기
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    cnt = 0
    while q1_sum != q2_sum:
        if cnt >= (len(queue1) + len(queue2))*2:
            return -1
        
        if q1_sum > q2_sum:
            temp = q1.popleft()
            q2.append(temp)
            cnt += 1
            q1_sum -= temp
            q2_sum += temp
        elif q1_sum < q2_sum:
            temp = q2.popleft()
            q1.append(temp)
            cnt += 1
            q1_sum += temp
            q2_sum -= temp
            
    return cnt if sum(q1) == sum(q2) else -1
from collections import Counter

def solution(k, tangerine):
    # 각 원소별로 개수가 몇개인지 확인
    # k개를 개수가 많은 순서대로 세기
    lst = sorted(Counter(tangerine).items(), key = lambda x:x[1], reverse=True)
    
    sum = 0
    answer = 0
    
    for _, v in lst:
        sum += v
        answer += 1
        if sum >= k:
            return answer
        

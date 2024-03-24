def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    
    for idx in range(m-1, len(score), m):
        answer += score[idx] * m
        
    return answer
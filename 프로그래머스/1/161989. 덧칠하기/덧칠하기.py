def solution(n, m, section):
    answer = 0
    
    dic = {i:True for i in range(1, n+1+m)}
    
    for sec in section:
        dic[sec] = False # 다시 칠해야 되는게 False
        
    for idx in range(1, n+1):
        if dic[idx] == False:
            for roll_len in range(m):
                dic[idx + roll_len] = True
            answer += 1
    
    return answer
def solution(n):
    
    n_cnt = 0
    for i in bin(n):
        if i == '1':
            n_cnt += 1

    next_num = n+1
    next_cnt = 0
    
    while True:
        for i in bin(next_num):
            if i == '1':
                next_cnt += 1
        if n_cnt == next_cnt:
            break
        else:
            next_cnt = 0
            next_num += 1
            
    return next_num 

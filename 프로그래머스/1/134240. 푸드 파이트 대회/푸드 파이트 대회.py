def solution(food):
    tmp = ""
    answer = ""
    
    for idx, calorie in enumerate(food):
        
        if idx == 0:
            continue
            
        tmp += str(int(calorie // 2) * str(idx))
    
    answer += tmp + "0"
    
    for i in range(len(tmp)-1, -1, -1):
        answer += tmp[i]

    return answer
        
    
        
            

            
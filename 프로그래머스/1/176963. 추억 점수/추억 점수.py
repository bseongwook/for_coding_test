def solution(name, yearning, photo):
    dic = {human : score for human, score in zip(name, yearning)}
    answer = []
    
    for p in photo:
        temp_sum = 0
        
        for human in p:
            if human in dic:
                temp_sum += dic[human]
        answer.append(temp_sum)
                
    return answer
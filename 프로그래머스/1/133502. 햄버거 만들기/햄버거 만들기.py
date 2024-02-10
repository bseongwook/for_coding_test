def solution(ingredient):
    answer = 0
    check_point = 0
    
    while True:
        for idx in range(check_point, len(ingredient)):
            if idx == len(ingredient)-1:
                return answer
            if ingredient[idx:idx+4] == [1,2,3,1]:
                del ingredient[idx:idx+4]
                answer += 1
                check_point = idx-3
                break

        
                
        
            
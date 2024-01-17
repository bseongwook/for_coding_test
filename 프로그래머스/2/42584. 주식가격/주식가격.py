def solution(prices):
    answer = []
    
    for idx in range(len(prices)-1): # 0~7
        
        i = idx+1
        
        while i < len(prices):
            if prices[idx] > prices[i]: # 떨어진 경우
                answer.append(i-idx)
                break
            else:
                i += 1
        
        if i == len(prices): # 끝까지 안떨어진 경우
            answer.append(len(prices) - idx - 1)
        
    answer.append(0)
    return answer
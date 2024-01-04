def solution(a, b, n):
    answer = 0
    
    while n >= a:
        
        temp_n = n
        n = (temp_n // a) * b
        
        answer += n
        
        n += temp_n % a
        
        
        
    return answer
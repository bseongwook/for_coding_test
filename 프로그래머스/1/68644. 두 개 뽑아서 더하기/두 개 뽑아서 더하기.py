def solution(numbers):
    s = set()
    
    for idx in range(len(numbers)-1):
        for j in range(idx+1, len(numbers)):
            s.add(numbers[idx]+numbers[j])
    
    answer = list(s)
    answer.sort()
    return answer
def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, target, idx, sum_so_far):
        if idx == len(numbers):
            if sum_so_far == target:
                return 1
            else: 
                return 0
        
        return dfs(numbers, target, idx + 1, sum_so_far + numbers[idx]) \
               + dfs(numbers, target, idx + 1, sum_so_far - numbers[idx])
          
    answer = dfs(numbers, target, 0, 0)
    
    return answer
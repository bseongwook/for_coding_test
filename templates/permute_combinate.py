# nums = [1,2,3,4]
# 로 만들 수 있는 모든 순열을 반환하시오

# 아래 순열, 조합, 부분집합 코드는 직접 그림그리고 코드 작성해보세요

def permute(nums):
    def backtrack(curr):
        if len(nums) == len(curr):
            ans.append(curr[:])
            return
        
        for num in nums: # 1,2,3,4중 하나 
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    
    ans = []
    backtrack()
    return ans


# nums = [1,2,3,4]에서
# 2개의 뭔소로 만들 수 있는 모든 순열을 반환하시오

def combinate(nums, k):
    result = []
    
    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

    backtracking(0, [])
    return result



# nums = [1,2,3,4]에서
# 만들 수 있는 부분집합을 모두 반환하시오
# 원소 개수에 따라 나눠

def sub_combinate(nums, k):
    result = []
    
    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

    for k in range(len(nums)+1):
        backtracking(0, [])
    return result



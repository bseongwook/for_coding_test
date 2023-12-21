# Two sum

# 기억하고 싶은게 있다면 key에다 넣는다. in 사용을 효과적으로 하기 위함
# value는 의미 없으므로 아무거나 집어넣기

def TwoSum(nums, target):
    memo = {}
    for n in nums: # O(n)
        memo[n] = 1
    
    for n in nums: # O(n)
        need_number = target - n
        if need_number in memo: # O(1)
            return True
        
    return False

print(TwoSum([1,2,3,4], 8))

# 단 위 코드에서는 같은 값을 2번 사용하여 target을 만들 수 있다.

def TwoSum(nums, target):
    memo = {}

    for n in nums:
        memo[n] = 1

    for n in nums:
        need_number = target - n
        if (need_number in memo) and n != need_number:
            return True
        
    return False

print(TwoSum([1,2,3,4], 8))
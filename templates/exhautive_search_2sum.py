# 리스트 [4,9,7,5,1]에서 K개의 숫자를 더해서
# 12가 될 수 있나? 중복 x

# k개의 for문을 쓸 수는 없으니 재귀로 구현

# len(curr) == k 해주면 해결??

def solution(nums, target):
    def backtrack(start, curr):
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr
        
        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtrack(i+1, curr)

            if ret:
                return ret
            
            curr.pop()
        return None
    return backtrack(0, [])

print(solution([4,9,7,5,1], 12))

# 내가 지금 선택한 state를 넣고 백트랙 한 뒤, 다 돌고 현재상태 빼줌
    






print(solution(nums=[4,9,7,5,1]))



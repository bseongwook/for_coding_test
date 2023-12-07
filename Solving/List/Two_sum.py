# step1 : 문제 이해
    # 문제 : 
    # 정수가 저장된 배열 nums, 원소중 2 숫자를 더해서 target이 될 수 있으면 T, 아니면 F 반환

    # 제약조건에서 10^8 넘으면 안됨
    # int 데이터는 4 바이트 : 32 비트이므로 이런 nums 원소 중 2개를 더해서 int 넘는지도 확인해야됨

# step2 : 접근 방법
    # 1. 직관적으로 생각 : 보통 완탐으로 시작,
        # 문제 상황 단순화, 문제 상황 극한화
    # 2. 자료구조와 알고리즘 사용
        # step1 문제 이해에서 파악한 내용을 토대로 자료구조 뭐 사용할지 결정
        # 대놓고 특정 자구 알골을 요구하는 경우 존재
        # 자구에 따라 선택할 수 있는 알고리즘을 문제에 적용
    # 3. 메모리 사용
        # 시간복잡도를 줄이기 위해 메모리를 사용하는 방법
        # 대표적으로 해시테이블

# 완탐으로 시작하면 (n^2) 정도 나옴, 이러면 시간 초과 걸림
# 실제로는 코드 작성 전에 시간 복잡도 계산하고 작성하기

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

twoSum(nums=[4,1,9,7,5,3,16], target=14)
# 어차피 시간복잡도 걸림
# nlogn이하 알고리즘 사용 - 정렬부터 생각 ####################### 이게 중요, 정렬하고 생각


# 정렬은 nlogn 시간복잡도 걸림
# 정렬하면 2 pointer 연관지어 생각
# 보통 2 pointer는 정렬이 된 상태에서 쓰임
# 양 끝에 포인터 놓고 하나씩 안으로 옮기면서 생각
# 같은 원소 선택 시 반복이 종료되게 설계

def twoPointer(nums, target):
    nums.sort()

    n = len(nums)
    l = 0
    r = n-1

    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        if nums[l] + nums[r] == target:
            return True

    return False

twoPointer(nums=[4,1,9,7,5,3,16], target=14)
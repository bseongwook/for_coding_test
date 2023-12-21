# longest consecutive sequence

# 먼저 한 숫자를 보고 뒤를 탐색함, n개의 숫자가 있을 경우 뒤에 남은 n-1개의 숫자에 대해 탐색해야함
# 

def longestConsecutive(nums):
    longest = 0

    # num_dict = {}
    # for num in nums:
    #     num_dict[num] = True

    # 굳이 위 처럼 딕셔너리 3줄로 만들지 말기
    # num_dict = set(nums)
    num_dict = {x : True for x in nums}

    for num in num_dict:
        if num-1 not in num_dict: # 전부 순회 x, O(1),  # 시작하는 수면 들어감
            cnt = 1 # 처음 숫자 자체
            target = num + 1 # 이어진 다음 숫자

            # for 안에 while 있으면 특정 조건을 만족할 때만 도는 것. n^2 아님
            # n개의 데이터가 있으면 for와 독립적으로 n번만 도는, n + n의 구조라고 보는게 합당

            while target in num_dict: # O(1)           # 다음 숫자 있으면 들어감
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

print(longestConsecutive([6,7,100,5,4,4]))


# 아래는 생각의 흐름

# for i in range(N):
#     while next in nums:
#         count += 1
#         next += 1

# 처음엔 대충 위와 같은 생각 가능, 시간 줄이기 위해 딕셔너리 사용가능 nums -> nums_dict
# 불필요하게 반복되는 확인 없애기 - if 앞선수 not in nums_dict

# for i in range(N):
#     if prev not in nums_dict: # 제일 작은 수부터 (시작점) 한 번만 반복될 것
#         while next in nums_dict:
#             count += 1

# 혹은 정렬부터 시작 nlogn







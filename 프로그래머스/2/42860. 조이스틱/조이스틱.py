# def solution(name): # print(ord('A'), ord('Z')) # 65, 90
#     answer = 0
#     check = [ "0" for _ in range(len(name)) ]
#     idx = 0 # 현재 커서 위치
    
#     while "0" in check:
#         if name[idx] != 'A':
#             forward = ord(name[idx]) - 65
#             answer += forward if forward <= (26 - forward) else (26 - forward)
#             check[idx] = "1"
#             for i in range(1, len(name)):
#                 target1 = (idx + i) % len(name)
#                 target2 = (len(name) - target1) % len(name)
#                 if name[target1] != 'A' and check[target1] == "0":
#                     idx = target1
#                     answer += i
#                     break
#                 elif name[target2] != 'A' and check[target2] == "0":
#                     idx = target2
#                     answer += i
#                     break
#                 if i == len(name) - 1:
#                     return answer
            
#         else:
#             check[idx] = "1"
#             for i in range(1, len(name)):
#                 target1 = (idx + i) % len(name)
#                 target2 = len(name) - target1
#                 if name[target1] != 'A' and check[target1] == "0":
#                     idx = target1
#                     answer += i
#                     break
#                 elif name[target2] != 'A' and check[target2] == "0":
#                     idx = target2
#                     answer += i
#                     break
#                 if i == len(name) - 1:
#                     return answer
#     return answer

def solution(name):
# 두번 꺽는 경우는 고려하지 않음

    if set(name) == {'A'}:
        return 0

    a_pos = ord('A') # 'A' : 65, 'Z' : 90
    z_pos = ord('Z')

    answer = float('inf')

    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] #왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i: :-1] + name[i+1:][::-1] # 기준점에서 빠꾸 + 좌측
        for n in [l_r,r_l]:
            # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c)-a_pos, (z_pos+1) - ord(c)) for c in n ]
            answer = min(answer, i + (len(cnt)-1) + sum(cnt))

    return answer
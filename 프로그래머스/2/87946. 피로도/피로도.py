from itertools import permutations

def solution(k_, dungeons):
    answer = 0
    
    for each_case in permutations(dungeons, len(dungeons)):
        # 따로 정렬하지 않으려고 permutations 씀
        # print(each_case) # ([80, 20], [50, 40], [30, 10])
        k = k_
        cnt = 0 # 해당 case로 탐험을 하면 방문할 수 있는 개수
        for dungeon in each_case:
            # print(dungeon)
            if dungeon[0] <= k:
                k -= dungeon[1]
                cnt += 1
        # print(cnt)
        answer = max(answer, cnt)
        
    return answer
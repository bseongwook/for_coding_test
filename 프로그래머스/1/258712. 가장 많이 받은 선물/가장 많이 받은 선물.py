from itertools import combinations

def solution(friends, gifts):
    
    name_dic = {name:i for i, name in enumerate(friends)}
    # print(name_dic) # dic1에서 사람 이름 대신 쓰일 인덱스
    
    dic1 = {name:[0]*len(friends) for name in friends}
    dic2 = {i:[0, 0, 0] for i in friends} # 준 / 받은 / 선물지수
    
    present = {name:0 for name in friends} # 사람별로 선물 받을 수
    
    for data in gifts: # dic1, dic2 만들기
        giver, taker = data.split()
        
        dic1[giver][name_dic[taker]] += 1
        
        dic2[giver][0] += 1
        dic2[taker][1] += 1
        
        dic2[giver][2] = dic2[giver][0] - dic2[giver][1]
        dic2[taker][2] = dic2[taker][0] - dic2[taker][1]
        
#     print(dic1) 
#     print(dic2)
    
    for p1, p2 in combinations(friends, 2):
        if dic1[p1][name_dic[p2]] > dic1[p2][name_dic[p1]]:
            present[p1] += 1
        elif dic1[p1][name_dic[p2]] < dic1[p2][name_dic[p1]]:
            present[p2] += 1
        else: # 선물 지수 비교
            if dic2[p1][2] > dic2[p2][2]:
                present[p1] += 1
            elif dic2[p1][2] < dic2[p2][2]:
                present[p2] += 1
    # print(present)
    return max(present.values())

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for food_num in course:
        dic = defaultdict(int)
        m_value = 2 # 2명 이상 시킨 메뉴들
        temp_lst = []
        # xy, yx랑 다른 키로 들어감
        for order in orders:
            for each_combi in combinations( list(order), food_num ):
                s = ""
                each_combi = sorted(each_combi)
                for string in each_combi:
                    s += string
                dic[s] += 1
                
        # print(dic)
        for k, v in dic.items():
            if v > m_value:
                m_value = v
                temp_lst = []
                temp_lst.append(k)
            elif v == m_value:
                temp_lst.append(k)  
        for i in temp_lst:
            answer.append(i)
    return sorted(answer)
#     answer = sorted([sorted(i) for i in answer])
#     new_answer = []
#     for i in answer:
#         new_answer.append(''.join(i))
        
#     return new_answer
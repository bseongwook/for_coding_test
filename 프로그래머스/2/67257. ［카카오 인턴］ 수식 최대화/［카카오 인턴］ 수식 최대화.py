from collections import deque
from itertools import permutations

def solution(expression):
    
    max_value = 0
    
    # 계산에 필요한 연산리스트, 숫자리스트 제작
    oper_lst_og = deque()
    num_lst_og = deque()
    temp = ""
    for i in expression:
        if not i.isdigit():
            oper_lst_og.append(i)
            num_lst_og.append(int(temp))
            temp = ""
        else:
            temp += i
    num_lst_og.append(int(temp))
    # num_lst_og = [50, 6, 3, 2]
    # oper_lst_og = ['*', '-', '*']     
    # print(oper_lst.index('*')) 
    
    operation_candidates = permutations(['*', '-', '+'])
    
    for operation_order in operation_candidates: # 6개의 경우 구성
        num_lst = deque(num_lst_og)
        oper_lst = deque(oper_lst_og)
        for aim_operator in operation_order: # 처리해야 될 연산자 결정 (+ 다 끝내고 - ...)
            idx = 0
            while idx < len(oper_lst):
                if oper_lst[idx] == aim_operator and aim_operator == '*':

                    cal_result = num_lst[idx] * num_lst[idx+1]
                    del num_lst[idx]
                    del num_lst[idx]
                    del oper_lst[idx]
                    num_lst.insert(idx, cal_result)

                elif oper_lst[idx] == aim_operator and aim_operator == '-':

                    cal_result = num_lst[idx] - num_lst[idx+1]
                    del num_lst[idx]
                    del num_lst[idx]
                    del oper_lst[idx]
                    num_lst.insert(idx, cal_result)

                elif oper_lst[idx] == aim_operator and aim_operator == '+':
                    cal_result = num_lst[idx] + num_lst[idx+1]
                    del num_lst[idx]
                    del num_lst[idx]
                    del oper_lst[idx]
                    num_lst.insert(idx, cal_result)
                else:
                    idx += 1
            if len(oper_lst) == 0:
                max_value = max( max_value, abs(num_lst.popleft()) )
                break

    return max_value
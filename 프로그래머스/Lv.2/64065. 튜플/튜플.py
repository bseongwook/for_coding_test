def solution(s):
    answer = []
    
    lst = []
    
    temp_lst = []
    reset_temp_lst = False
    temp_num = ''
    
    for char in s[1:-1]:
        
        if char == '{':
            reset_temp_lst = False
            
        elif char == '}':
            reset_temp_lst = True
            temp_lst.append(int(temp_num))
            temp_num = ''
            
        elif char == ',' and reset_temp_lst:
            lst.append(temp_lst)
            temp_lst = []
            
        elif char == ',' and not reset_temp_lst:
            temp_lst.append(int(temp_num))
            temp_num = ''
            
        else:
            temp_num += char
            
    lst.append(temp_lst)
    lst.sort(key = lambda x : len(x))
    
    for elements in lst:
        for i in elements:
            if i not in answer:
                answer.append(i)
    return answer
    
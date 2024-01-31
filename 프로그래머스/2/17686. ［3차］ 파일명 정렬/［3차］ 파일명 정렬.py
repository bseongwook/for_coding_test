def solution(files):
    answer = []
    
    for file in files:
        HEAD = ''
        NUMBER = ''
        TAIL = ''
        done_head = False
        done_number = False
        # 숫자가 6개인 경우도 고려 - 붙어있진 않았음
        for f in file:
            if not done_head and not f.isdigit():
                HEAD += f
            elif not done_number and f.isdigit():
                NUMBER += f
                done_head = True
            else:
                done_number = True
                TAIL += f
        answer.append((HEAD, NUMBER, TAIL))
        
    answer.sort(key = lambda x: (x[0].lower(), int(x[1]) ))
    lst = []
    for i in answer:
        lst.append("".join(i))
    return lst
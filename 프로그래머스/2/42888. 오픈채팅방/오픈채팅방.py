def solution(record):
    
    # dict에 id별 닉네임 저장
    dic = {}
    
    for r in record:
        splited_r =  r.split()
        
        if splited_r[0] == "Enter":
            dic[splited_r[1]] = splited_r[2]
        elif splited_r[0] == "Change":
            dic[splited_r[1]] = splited_r[2]

    answer = []
    for r in record:
        splited_r =  r.split()
        
        if splited_r[0] == "Enter":
            answer.append(f"{dic[splited_r[1]]}님이 들어왔습니다.")
        elif splited_r[0] == "Leave":
            answer.append(f"{dic[splited_r[1]]}님이 나갔습니다.")

    return answer  
            
    # enter, leave일 경우에 맞춰 이름 바꿔서 문자열 저장
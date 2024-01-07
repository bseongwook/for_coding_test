def solution(today, terms, privacies):
    terms_dic = {term.split()[0]:term.split()[1] for term in terms}
    # print(terms_dic)     {'A': '6', 'B': '12', 'C': '3'}
    
    answer = []
    
    t_year = int(today.split('.')[0])
    t_month = int(today.split('.')[1])
    t_day = int(today.split('.')[2])
    
    # day 기준으로 계산할 것 / 1년은 336일, 1달은 28일
    for idx, p in enumerate(privacies):
        val_month = int(terms_dic[ p.split()[1] ]) # 해당 p의 약관 종류에 대한 유효기간
        
        p_year = int(p.split()[0].split('.')[0])
        p_month = int(p.split()[0].split('.')[1])
        p_day = int(p.split()[0].split('.')[2])
        
        if (t_year*336 + t_month*28 + t_day) - (p_year*336 + p_month*28 + p_day) >= val_month * 28:
            answer.append(idx+1)
    
    return answer

    
    
    
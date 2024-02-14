def solution(survey, choices):
    
    answer = ""
    
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for surv, ch in zip(survey, choices):
        if ch >= 5:
            dic[surv[1]] += score[ch]
        else:
            dic[surv[0]] += score[ch]
            
    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += 'C' if dic['C'] >= dic['F'] else 'F'
    answer += 'J' if dic['J'] >= dic['M'] else 'M'
    answer += 'A' if dic['A'] >= dic['N'] else 'N'
    
    return answer
        
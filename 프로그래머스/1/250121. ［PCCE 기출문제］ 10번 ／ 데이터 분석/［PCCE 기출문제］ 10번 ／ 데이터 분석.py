def solution(data, ext, val_ext, sort_by):
    answer = []
    
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    for data_row in data:
        if data_row[ dic[ext] ] <= val_ext:
            answer.append(data_row)
    
    answer.sort(key = lambda x : x[dic[sort_by]] )
    
    return answer
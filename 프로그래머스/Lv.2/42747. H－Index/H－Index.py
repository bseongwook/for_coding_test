def solution(citations):

    citations.sort(reverse = True) # 	[8,7,6,5,0]
    
    h_index = citations[0] # 최대값, 이후 -1씩
    for h in range( citations[0], -1, -1 ): # 8 ~ 0
        # range 오류 방지, 해당 인덱스의 숫자크기를 확인함으로써 
        # h_index보다 큰 숫자가 몇개인지 확인가능 
        if len(citations) > h-1 and citations[h-1] >= h_index:
            return h
        else:
            h_index -= 1
    
    
        
            
            
        
        
        
        
    
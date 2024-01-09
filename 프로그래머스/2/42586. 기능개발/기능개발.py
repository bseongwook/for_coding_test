from collections import deque
import math

def solution(progresses, speeds):
    
    idx = 0
    answer = []
    
    for day in range(1, 101): # 하루에 1퍼는 하니까 최대 100일 걸림
        
        if len(progresses)-1 == idx and progresses[-1] >= 100:
            break
        
        for i, s in enumerate(speeds): # for문 돌면 하루의 끝 도달
            if i < len(progresses):
                progresses[i] += s
        
        # print(progresses)
        cnt = 0  # 한 번에 배포될 수 있는 기능 수
        flg = False
        
        while idx <= len(progresses)-1 and progresses[idx] >= 100:
            idx += 1
            cnt += 1
            flg = True
            
        if flg:
            answer.append(cnt)
        
    return answer
    
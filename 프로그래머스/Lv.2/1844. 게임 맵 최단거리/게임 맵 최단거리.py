from collections import deque

def solution(maps):
    
    # 최단 경로 문제의 경우 방문 노드의 위치와 함께 해당 노드를 몇번째로 방문했는지도 같이 저장하면 좋다
    
    answer = 0
    
    # if maps[-1][-2] == 0 and maps[-2][-1] == 0: # 도달 못하는 경우
    #     return -1
    # 중간에 끊어진 경우도 존재하니까 제외하고 시작할 수 없다
    
    col = len(maps[0])
    row = len(maps)
    
    q = deque()
    q.append((0,0,1)) # 좌표, 해당 위치를 방문할 경우의 진행한 칸 개수
    maps[0][0] = 0 # 방문 처리
    
    # 하 우 좌 상
    dx = [0, 1,-1,0]
    dy = [1, 0, 0,-1]    
    
    while q:
        answer = 0
        cur_position = q.popleft()
        # print(cur_position[0], cur_position[1])
        answer += cur_position[2] + 1
        
        if (cur_position[0], cur_position[1]) == (row-1, col-1):
            return answer-1
        
        for i in range(4):
            new_x = cur_position[0] + dx[i]
            new_y = cur_position[1] + dy[i]
            if -1 >= new_x or new_x >= row or -1 >= new_y or new_y >= col:
                continue
            if (maps[new_x][new_y] == 1):
                maps[new_x][new_y] = 0
                q.append((new_x, new_y, answer))
                
    return -1


    
    
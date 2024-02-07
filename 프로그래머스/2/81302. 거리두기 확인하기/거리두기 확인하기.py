def manh_error(row, col, temp_map):
    
    dx = [0,0,-1,1] # 상하좌우
    dy = [-1,1,0,0] # 아래로 가야 y 증가
    
    for i in range(4): # 한 방향씩 확인
        new_x = row + dx[i]
        new_y = col + dy[i]
        
        if new_x < 0 or new_x > 4 or new_y < 0 or new_y > 4: # 범위 나감
            continue
            
        if temp_map[new_x][new_y] == 'P': # 상하좌우로 사람 있으면
            return True
        elif temp_map[new_x][new_y] == 'X':
            continue
        else: # temp_map[new_x][new_y] == 'O' - 여기서 잡아낼 것
            for j in range(4):
                new_new_x = new_x + dx[j]
                new_new_y = new_y + dy[j]
                
                if ((new_new_x, new_new_y) != (row, col)) \
                and 0<=new_new_x<=4 and 0<=new_new_y<=4:
                    if temp_map[new_new_x][new_new_y] == 'P':
                        return True
        
    return False
            
def solution(places):
    answer = [1,1,1,1,1]
    idx = 0
    
    for room in places: # room = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
        temp_map = [ [''] * 5 for _ in range(5) ]
        
        for row in range(5):
            for col in range(5):
                temp_map[row][col] = room[row][col]
        
        for row in range(5):
            for col in range(5):
                if temp_map[row][col] == 'P': # 맨해튼 거리 판단, 하나라도 걸리면 
                    if manh_error(row, col, temp_map):
                        answer[idx] = 0
        idx += 1
        
    return answer      
    
    
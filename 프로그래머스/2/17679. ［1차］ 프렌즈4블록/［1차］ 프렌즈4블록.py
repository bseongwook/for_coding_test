def solution(m, n, board):
    # 전체 지도 만들기
    temp_map = [ [board[r][c], False] for r in range(len(board)) for c in range(len(board[0])) ]
    map_ = []
    temp_lst = []
    for element in temp_map:
        temp_lst.append(element)
        if len(temp_lst) == n:
            map_.append(temp_lst)
            temp_lst = []
    
    will_be_removed = True # 한 번은 봐라
    # 삭제할 게 없을 때 까지 반복
    while will_be_removed:
        will_be_removed = False # 한 번은 봐라
        
        # 삭제할 것들 체크
        for row in range(m-1):
            for col in range(n-1):
                creterion = map_[row][col][0]
                if creterion != '':
                    if map_[row+1][col][0] == creterion and \
                    map_[row][col+1][0] == creterion and \
                    map_[row+1][col+1][0] == creterion:
                        will_be_removed = True
                        map_[row][col][1] = True
                        map_[row+1][col][1] = True
                        map_[row][col+1][1] = True
                        map_[row+1][col+1][1] = True

        # 삭제 후 자리 빈 칸 유지
        for row in range(m):
            for col in range(n):
                if map_[row][col][1]:
                    map_[row][col][0] = ''
                    map_[row][col][1] = False

        # 아래로 내리기
        # 우측 하단에서부터 좌측 상단까지 원소들 체크하며, 아래에 빈 자리가 있을 경우 끝까지 내리고 빈칸 처리
        for row in range(m-2, -1, -1):
            for col in range(n-1, -1, -1):
                if map_[row][col][0] != '' and map_[row+1][col][0] == '': # 원소발견 후 아래 빈 칸
                    go_down = 1
                    have_switch = False # 맨 밑 줄에서 범위 벗어나면 변수 안바뀜
                    while row + go_down < m:
                        have_switch = True
                        if map_[row + go_down][col][0] == '':
                            go_down += 1
                        else:
                            have_switch = False
                            map_[row + go_down - 1][col][0], map_[row][col][0] =\
                            map_[row][col][0], map_[row + go_down - 1][col][0]
                            break
                    if have_switch:
                        map_[row + go_down - 1][col][0], map_[row][col][0] =\
                        map_[row][col][0], map_[row + go_down - 1][col][0]
        
    answer = 0  
    for r in range(m):
        for c in range(n):
            if map_[r][c][0] == '':
                answer += 1
                
    return answer
                

def solution(board, h, w):
    answer = 0
    
    b_len = len(board)
    
    dh = [1, -1, 0, 0]
    dw = [0, 0, 1, -1]
    
    cur_color = board[h][w]
    
    for i in range(4):
        new_h = h + dh[i]
        new_w = w + dw[i]
        
        if (0 <= new_h <= b_len - 1) and (0 <= new_w <= b_len - 1):
            if cur_color == board[new_h][new_w]:
                answer += 1
    
    return answer
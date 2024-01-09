
def solution(brown, yellow):
    
    for y_col in range(1, yellow+1):
        if yellow % y_col == 0: # 약수라면
            y_row = yellow // y_col
        
        if (y_col+2)*(y_row+2) == brown + yellow:
            return [y_row+2, y_col+2]
        
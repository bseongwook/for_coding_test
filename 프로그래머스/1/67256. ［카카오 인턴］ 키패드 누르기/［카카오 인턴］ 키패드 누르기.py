
def solution(numbers, hand):
    answer = ''
    
    dic = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), \
            6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    
    l_hand = [3,0] # y,x
    r_hand = [3,2]
    
    for num in numbers:
        if num in [1,4,7]:
            l_hand = [dic[num][0], dic[num][1]]
            answer += 'L'
        elif num in [3,6,9]:
            r_hand = [dic[num][0], dic[num][1]]
            answer += 'R'
        else: # 2,5,8,0
            # 거리 측정 - 피타고라스는 대각선이라 안됨
            # (l_hand[0]-dic[num][0])**2 + (l_hand[1]-dic[num][1])**2 불가능
            l_dist = abs(l_hand[0]-dic[num][0]) + abs(l_hand[1]-dic[num][1])
            r_dist = abs(r_hand[0]-dic[num][0]) + abs(r_hand[1]-dic[num][1])
            print(l_dist, r_dist)
            if l_dist == r_dist:
                if hand == 'right':
                    answer += 'R'
                    r_hand = [dic[num][0], dic[num][1]]
                else:
                    answer += 'L'
                    l_hand = [dic[num][0], dic[num][1]]
            elif l_dist > r_dist:
                answer += 'R'
                r_hand = [dic[num][0], dic[num][1]]
            else:
                answer += 'L'
                l_hand = [dic[num][0], dic[num][1]]
                  
    return answer
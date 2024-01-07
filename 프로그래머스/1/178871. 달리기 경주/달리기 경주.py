import collections
def solution(players, callings):
    p = {p_:idx for idx, p_ in enumerate(players)} # 현재 등수
    
    for name in callings:
        idx = p[name]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        p[players[idx-1]] -= 1
        p[players[idx]] += 1
    return players
 

import sys
sys.setrecursionlimit(10 ** 6)

map_ = []
for row in range(5):
    map_.append(list(map(str, input().split())))

dic = {} 
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]
visited = []

def dfs(cur_x, cur_y, cur_string):
    cur_string += map_[cur_x][cur_y]

    if len(cur_string) == 6:
        dic[cur_string] = True
        return

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x <= 4 and 0 <= next_y <= 4:
            dfs(next_x, next_y, cur_string)

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(dic))

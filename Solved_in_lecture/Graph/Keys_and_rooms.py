# 0 ~ n-1번 방까지 라는 문구가 있다면 배열 쓰기에 적합할지도

# 방 개수는 시간 복잡도에 영향을 주는 요소 n
# 1000까지니까 n^2으로 가능

# 서로 연결된 방은 그래프로 생각가능, 열쇠없는 방이면 떨어진 노드로 그리기

from collections import deque

def canVisitALLrooms(rooms):
    # visited = []
    visited = {} # dfs용
    # visited = [False] * len(rooms) # bfs용

    # vertex에 연결되어 있는 모든 v 방문할거다
    def dfs(v):
        visited[v] = True # True는 의미 없는 값이지만 딕셔너리 사용을 위해
        # 아니면 in으로 확인하지 말고 미리 visited = [False]* len(rooms)로 만든 다음,
        # 인덱스 찾아서 바로 비교

        for next_v in rooms[v]: # list은 n만큼 걸림, hash는 1만큼 걸림
            if next_v not in visited: # 이거 없으면 무한 반복
                dfs(next_v)
    
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True
        while q:
            cur_v =q.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    q.append(next_v)
                    visited[next_v] = True

    dfs(0)
    return True if len(rooms) == len(visited) else False


rooms = [[1,3], [2,4], [0],[4],[],[3,4]]
print(canVisitALLrooms(rooms))


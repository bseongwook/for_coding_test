# 주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블 붙어 있음
# times[i] = (u, v, w) : u에서 신호를 보내서 v노드에 도달하는데 걸리는 시간:w

# k노드에서 신호를 보낼 때. 모든 노드에 신호가 도달하기 위한 최소비용 반환해
# 하나의 노드라도 도달하지 못한다면 -1 반환
# 한 노드에서 연결된 여러개의 edge에 신호를 동시에 전달할 수 있다.

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= u, v <= n
# u != v
# 1 <= w <= 100
# 모든 (u,v)쌍은 unique

# ------------------------------------------------------------------------

# 이 문제는 가중치가 존재하므로 다익스트라로 풀어야 함
# 혹은 최단 경로 알고리즘

# 문제풀이 순서는 다음과 같다

# 1 .그래프 구현                O(times.length) 6000
# 2. 다익스트라 알고리즘        O(times.legnth log times.legnth) 10^5
# 3. 방문 못한 노드 찾기        O(n) 100
# 4. 최소값중에서 최대값 구하기 O(n) 100

import heapq
from collections import defaultdict

def ndt(times, n, k):
    # 1번
    graph = defaultdict(list)
    for time in times:
        graph[times[0]].append((time[2], time[1]))

    # 2번
    costs = {}
    pq = [] 
    heapq.heapify(pq) 
    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost 
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    # 3번
    for node in range(1, n+1):
        if node not in costs:
            return -1
    
    # 4번
    return max(costs.values())

    



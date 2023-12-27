import heapq

def dijkstra(graph, start, final): # start, final은 노드 이름
    costs = {}
    pq = []   # 우선순위 큐
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    return cost[final]

# 순서
# 1. 우선순위 큐에 시작 노드 추가
#     2. 우선순위가 가장 높은 노드 추출
#     3. 방문한 적 없다면 아래 4, 5 실행
#         4. 비용 업데이트
#         5. 현재 노드와 연결된 노드 우선순위 큐에 추가
# 6. 큐가 비면 목적지에 기록된 비용 반환


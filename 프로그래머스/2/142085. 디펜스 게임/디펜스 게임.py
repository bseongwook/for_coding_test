import heapq
# 어떤 리스트에서 최대, 최소 값을 찾을 때는 heap 자료구조 고려

# def solution(n, k, enemy):

#     heap = []
#     # heap의 길이(라운드 수)가 k보다 커질 때 pop 해주기
#     # 지나온 애들 중 가장 많은 적들일 때 무적권을 사용한 효과 - 최대 힙 사용하는 방법 알기
#     for idx, i in enumerate(enemy):
#         n -= i
#         heapq.heappush(heap, (-i, i))
        
#         if len(heap) > k:
#             n += heapq.heappop(heap)[1]
#             k -= 1
        
#         if k == 0 and n < 0:
#             return idx
        
#     return len(heap)

def solution(n, k, enemy):
    h = []
    
    for i, e in enumerate(enemy):
        heapq.heappush(h, e)
        if len(h) > k:
            n -= heapq.heappop(h) # 왜 최소힙으로 빼는거? 최대힙써야 되는게 아니라?
        if n < 0:
            return i

    return len(enemy)


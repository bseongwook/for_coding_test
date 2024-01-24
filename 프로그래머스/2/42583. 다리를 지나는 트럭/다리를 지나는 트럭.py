from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weight = [ [i, 0] for i in truck_weights] # 각 트럭별로 다리 위에 올라가있는 시간도 같이 표기
    waiting = deque(truck_weight)
    bridge = deque()
    done = []

    sec = 0
    while len(done) != len(truck_weights):
        sec += 1

        
        sum_ = 0
        for truck in bridge:
            sum_ += truck[0]
        if len(waiting) >= 1 and sum_ + waiting[0][0] <= weight: # 올릴 수 있으면 트럭 올려
            bridge.append(waiting.popleft())
        
        for truck in bridge: # 다리 위의 모든 트럭 한 칸 전진(1초 경과)
            truck[1] += 1
            
        if bridge[0][1] == bridge_length: # 끝까지 도달한 트럭 내려
            done.append(bridge.popleft())
    
    return sec + 1

        
        
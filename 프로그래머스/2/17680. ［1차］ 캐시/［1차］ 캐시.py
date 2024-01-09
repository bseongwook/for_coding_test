from collections import deque

def solution(cacheSize, cities):
    # linkedlist 문제
    # https://dailylifeofdeveloper.tistory.com/355
    time = 0
    
    q = deque()
    
    for city in cities:
        city = city.lower()
        if city not in q:
            q.append(city)
            time += 5
            if len(q) > cacheSize:
                q.popleft()
        else:
            q.remove(city)
            time += 1
            q.append(city)
            
    return time
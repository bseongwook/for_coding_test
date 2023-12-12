# 제약조건에서 input list 길이가 10^5 면 최대 O(N log n)

# 괄호 유효성 문제와 같이 특정 조건에서만 반응함
# 다만 특정 수치가 하나 들어올 떄 여러 온도에 반응하게 할 수 있다.
# 이미 영향을 받은 수치는 더 이상 영향받지 않는다.

# 숫자 낮은 애들은 스택에 쌓다가, 큰 애 들어오면 작은애들 전부 pop
# 다 뽑아낼 수 없다면 그냥 스택에 쌓임
# 스택에 저장할 때 날짜까지(인덱스까지) 저장해주는게 좋다

# 결과적으로 전체 리스트를 한 번만 훑으면서 O(N)으로 문제풀이 가능, append, pop은 O(1)이므로 영향 x

temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temperatures):

    stk = []
    answer = [0] * len(temperatures) 

    for cur_day, cur_temp in enumerate(temperatures): # 결국 한 번은 전부 확인해야 됨
        while stk and stk[-1][1] < cur_temp: # 만약 스택이 차있고, 온도가 현재의 온도보다 낮다면
            prev_day, _ = stk.pop() # pop()에서 버릴 값은 _로 받고 버림 
            answer[prev_day] = cur_day - prev_day
        stk.append((cur_day, cur_temp))

    return answer

# while 루프는 for 루프 내부에 중첩되지 않고 for 루프의 범위 내에 있습니다.
# 즉, while 루프는 for 루프의 각 반복마다 실행되지만 외부 루프의 각 반복마다 새로운 독립 루프를 생성하지는 않습니다.

# 따라서 전체 시간 복잡도를 분석할 때 for 루프와 while 루프의 시간 복잡도를 곱하지 않습니다.
# 입력 배열의 각 요소(온도)가 최대 한 번만 처리되므로 시간 복잡도는 O(N)으로 유지되며, 
# 배열의 길이에 비례하여 선형적인 시간 복잡도를 갖게 됩니다.




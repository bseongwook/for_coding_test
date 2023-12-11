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

# while은 temperature의 각 온도에 대해서 한 번씩만 연산되기 때문에 중첩이어도 n^2 아님
# 이건 2개의 반복문이 각각 독립적으로 시행되기 때문에 연속된 중첩이 아니라 병렬로 봐야됨
# 아래는 병렬의 예시

for i in range(10):
    for j in range(10):
        # Some O(1) operation
        print('a')

# 내부 반복문은 상수 시간의 작업을 수행하므로 O(N)이지만, 
# 루프가 상호 간섭없이 실행되기 때문에 병렬로 간주





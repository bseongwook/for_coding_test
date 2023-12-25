# 계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다. 한 번 올라갈 때마다
# 1, 2만큼 올라갈 수 있다. 꼭대기 도달하는 방법의 개수는 총 몇 가지?

# 제약조건 : 1 <= n <= 45


# =============== 풀이 ==================================================================

# 갈 수 있는 모든 경우 다 따지는 것 : 완탐


# 일단은 재귀로 생각
# 예를 들어 5층에 오려면 3 or 4층에서 오는 방법이 존재
# 이런 식으로 하위 문제로 나누기

def cs(n): # n층까지 갈 수 있는 모든 경우의 수
    if n == 1:
        return 1
    if n == 2:
        return 2
    return cs(n-1) + cs(n-2)


# 아래는 memoization을 적용한 과정 - top down

memo = {}
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)
    return memo[n]


# 아래는 bottom up으로 작성한 예시

memo = {1:1, 2:2}
def cs(n):
    for i in range(3, n+1):
        memo[n] = memo[i-1] + memo[i-2]
    return memo[n]
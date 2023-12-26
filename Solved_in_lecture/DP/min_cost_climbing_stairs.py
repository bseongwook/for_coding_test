# 계단을 올라가고 있는데, 한번에 1, 2만큼만 올라가기 가능
# 정수형 배열 cost가 주어지는데, cost[i]는 해당 계단을 밟았을때 지불하는 비용
# 시작은 0, 1 중 한 곳에서 가능
# 계단의 꼭대기에 도착하기 위해 지불해야 하는 비용의 최솟값 반환해

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999 : 여기는 무조건 밟는게 좋을듯, cost없이 최소 1칸을 올라가니


# 접근 방법 1 : 완전 탐색
# 재귀를 이용할 것이니 꼭대기의 입장에서 생각
# 꼭대기에 가려면, 전 계단과 그 전 계단에서 올라오는 경우 2가지 밖에 없음
# 재귀적으로 위에서부터 한 단계씩 확장해감
cost = [10, 15, 20, 17, 1]
def dfs(n):
    if n == 0 or n == 1:
        return 0
    return min(dfs(n-1)+cost[n-1], dfs(n-2)+cost[n-2]) # 1층 전에서 올라오거나, 2층 전에서 올라오는 경우
# 위 과정은 2^n이라서 시간초과남


# 접근 방법 2 : memoization 이용한 top_down 방식
memo = {}
def dp(n):
    if n == 0 and n == 1:
        return 0
    if n not in memo:
        memo[n] = min(dfs(n-1)+cost[n-1], dfs(n-2)+cost[n-2])
    return memo[n]
# 여기선 시간복잡도가 n, 이전에 계산한 적 없는 한 번만 계산하면 됨


# 접근 방법 3 : tabulation 이용한 bottom_up 방식 : 강의 후편 참고
def dp(n):
    memo = [-1] * n
    memo[0] = 0
    memo[1] = 0

    for i in range(2, n+1):
        memo[i] = min(dfs(i-1)+cost[i-1], dfs(i-2)+cost[i-2])
    return memo[n]
# 접근 방법 2 <-> 3 변환 필수
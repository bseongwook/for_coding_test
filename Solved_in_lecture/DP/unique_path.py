# 로봇은 m*n 격자 위에 존재, 처음엔 좌상단에 위치, 우하단이 목적지
# 한 번에 오른쪽, 아래로 움직이기 가능
# 두 정수 m,n이 주어졌을 때, 로봇이 우하단에 도달 가능한 path수 반환
# 1 <= m,n <= 100
# 테스트케이스는 답이 2*10^9 이하가 되도록 생성됨.
    # 2^31 은 2*10^9 비슷함 = 완탐으로 하면 무조건 시간초과
# 그렇기 때문에 메모리 사용해서 dp로 접근


# 접근방법1 : 완탐 : 격자는 그래프라고 생각
# 조합 사용해서 오른쪽화살표, 아래화살표 위치 생각하면 풀림
# 최대는 198C99 = 2 * 10^58
# 이 문제는 제약조건때문에 못하지만, 제약이 바뀔 수도 있으니 풀어보기
# 결국 우하단 가려면 우하단 왼쪽, 위쪽 블럭을 지나야됨
def dfs(r, c):
    if r == 2 and c == 6:
        return 1
    unique_path = 0
    if r+1 < 3: # 이동 공간 테두리 제한
        unique_path += dfs(r+1, c)
    if c+1 < 7:
        unique_path += dfs(r, c+1)
    return unique_path


# 접근방법2: top down : O(m*n) 수준
memo = {}
def dp(r, c):
    if r == 0 and c == 0:
        return 1
    if (r,c) not in memo:
        if r-1 >= 0:
            unique_path += dp(r-1, c)
        if c-1 >= 0:
            unique_path += dp(r, c-1)
        memo[(r,c)] = unique_path
    return memo[(r,c)] # 그냥 갖다 쓰더라도 한 번은 위에서 계산해야 됨


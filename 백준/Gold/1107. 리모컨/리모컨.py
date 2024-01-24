import sys

N = int(input()) # 이동하려고 하는 채널
M = int(input())

if M >= 2:
    impossible = list(map(int, input().split()))
elif M == 1:
    impossible = [int(input())]
elif M == 0:
    impossible = []

if N == 100:
    print(0)
    sys.exit(0)

# 최소로 가려면 n과 가장 가까운 숫자 - impossible 제외하고
# N +- i 두 숫자를 뽑아서 impossible 내부의 숫자가 없는지 전부 검사
# 각 경우별로 리스트에 담아서 최소값 출력하기
# 88 / 2 / 8 9의 경우, 그냥 + - 버튼으로 이동하는게 더 빠름 -> 이런 경우까지 리스트 추가

lst = []
for i in range(500000):
    a = str(N - i)
    b = str(N + i)

    sh1 = True
    if N - i >= 0:
        for forbidden in impossible:
            if str(forbidden) in a:
                sh1 = False
                break
        if sh1:
            lst.append(len(a)+i)
            # print('case1')
            break

    sh2 = True
    for forbidden in impossible:
        if str(forbidden) in b:
            sh2 = False
            break
    if sh2:
        lst.append(len(b)+i)
        # print('case2')
        break
        
lst.append(abs(100 - N))
print(min(lst))
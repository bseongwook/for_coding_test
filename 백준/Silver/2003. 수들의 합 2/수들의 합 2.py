N, target = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0 # 경우의 수

lft = 0
rgt = 0
s = sum( lst[lft:rgt+1] )

while rgt < N:
    # print(lft, rgt, s)

    if s < target:
        # print(" s < target ")
        rgt += 1
        if rgt != N:
            s += lst[rgt]
        else: 
            break
        
    elif s == target:
        # print(" s == target ")
        answer += 1
        s -= lst[lft]
        lft += 1

    elif s > target:
        # print(" s > target ")
        s -= lst[lft]
        lft += 1


print(answer)

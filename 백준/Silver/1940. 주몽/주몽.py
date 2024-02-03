N = int(input()) # 재료 개수
target = int(input())

ingredients = list(map(int, input().split()))

lft = 0
rgt = N-1

answer = 0

ingredients.sort() # 1, 2, 3, 4, 5, 7

while rgt > lft:
    if ingredients[rgt] + ingredients[lft] < target:
        lft += 1
    elif ingredients[rgt] + ingredients[lft] > target:
        rgt -= 1
    else:
        answer += 1
        rgt -= 1

print(answer)


t = int(input())

for _ in range(t):
    st = input()
    cum_score = 0
    final_score = 0

    for s in st:
        if s == 'O':
            cum_score += 1
            final_score += cum_score
        else:
            cum_score = 0
    
    print(final_score)
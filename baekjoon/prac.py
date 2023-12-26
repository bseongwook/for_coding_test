from collections import Counter

st = input().upper()

s= Counter(st).most_common()

if len(s) == 1:
    print(s[0][0])
elif s[1][1] == s[0][1]:
    print('?')
else:
    print(s[0][0])

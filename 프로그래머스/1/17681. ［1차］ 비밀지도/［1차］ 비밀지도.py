def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        st = ""
        print(bin(a1 | a2)[2:])
        for i in bin(a1 | a2)[2:]:
            if i == '1':
                st += '#'
            else:
                st += ' '
        if len(st) != n:
            st = ' '*(n-len(st)) + st 
        answer.append(st)
        
    return answer
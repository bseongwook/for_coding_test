def solution(s):
    answer = len(s)
    
    for num_of_char in range(1, int(len(s)/2)+1 ): # 자를 단위
        
        lst = []
        string = ""
        for idx in range(0, len(s), num_of_char):
            lst.append( s[idx : idx + num_of_char] ) # 이거 왜 인덱스 오류 안나??
        # print(lst)
        
        temp_str = lst[0]
        cnt = 1
        
        for i in range(1, len(lst)):
            if temp_str != lst[i]: # 앞 단어랑 다른 경우
                if cnt != 1:
                    string += str(cnt) + temp_str
                    cnt = 1
                else:
                    string += temp_str
                temp_str = lst[i]
            else:
                cnt += 1
                
        # for문 종료되고 temp-str에 남은 단어 처리
        if cnt != 1:
            string += str(cnt) + temp_str
            cnt = 1
        else:
            string += temp_str
        
        if len(string) < answer:
            answer = len(string)

    return answer
        
        
        
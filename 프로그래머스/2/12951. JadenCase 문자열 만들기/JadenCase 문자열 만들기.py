def solution(s):
    answer = ""
    if s[0].isalpha():
        answer += s[0].upper()
    else:
        answer += s[0]
        
    for i in s[1:]: # answer 마지막 글자가 공백이라면
        if i == " " or i.isdigit():
            answer += i
        else:
            if answer[-1] == " ":
                answer += i.upper()
            else:
                answer += i.lower()
            
    return answer
        
# 괄호 유효성 문제

# 소괄호부터 생각 : 1. 짝수일것, 2. 여는게 먼저, ,,,
# 모든 괄호 포함해서 생각, 마지막에 열린애를 닫기 전에 다른게 열리면 안됨 ( [ ) ] x
# stack 구조의 맨 위에 있는 놈 확인하고 닫아도 되는지 확인

def isVaild(s):
    stk = []
    for p in s:
        if p == "(":
            stk.append(")")
        elif p == "[":
            stk.append("]")
        elif p == "{":
            stk.append("}")
        elif not stk or stk.pop() != p: # 같으면 return 만나고 끝, 다르면 pop만 하고 넘어감
            return False
    return not stk # 다 반환됐으면 true
        

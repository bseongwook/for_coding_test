# 링크드리스트는 다음의 경우에 사용
    # 선형 자료구조 + 중간에 데이터 추가/삭제가 용이할 때 사용
    # tree / graph에 사용

# step 1 : 문제 이해하기
    # input, output 확인
        # 자료형? 값 크기의 범위? 마이너스 가능? 
        # 내가 어떤 값 반환해야 하는지, 정해진 형식대로 반환하려면 어떻게 구현할지
    # input size N 확인
        # 시간복잡도를 계산하기 위한 N 또는 M이 무엇인지 확인
    # 제약조건 확인
        # 시간복잡도 제한 있는지 확인
        # 내가 선택할 수 있는 알고리즘이 무엇이 있는지
    # 예생할 수 있는 오류 파악
        # 입력값 범위, stack overflow

# leetcode 1472

# 보통 완탐으로 시작 - 단순화, 극한화하며 생각
# 안되면 자구, 알골 활용, 자구에 따라 선택할 수 있는 알고리즘을 문제에 적용
# 시간복잡도를 줄이기 위해 메모리 사용(해시테이블)]

# 이 문제에서는 순서가 필요하다고 느낄 수 있다. 앞,뒤만 이동하니 선형 자료구조 사용가능
# 각 연산 별로 worstcase 생각 - 10^8 아래인지 확인

class ListNode(object):

    def __init__(self, val: str, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = ListNode(val = homepage)

    def visit(self, url: str): 
        self.current.next = ListNode(val = url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps: int):
        while steps > 0 and self.current.prev != None: # 더 이상 갈 곳이 없을 때까지
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
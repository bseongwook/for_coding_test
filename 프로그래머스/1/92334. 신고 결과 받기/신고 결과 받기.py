def solution(id_list, report, k):
    
    # 유저별로 신고한 사람 저장 - 이후 set을 통해 중복 처리
    report_dic = {i:set() for i in id_list}
    for i in report:
        report_dic[i.split()[0]].add(i.split()[1])    
    # print(report_dic)
    
    # 사람별로 신고 당한 횟수 저장
    reported_dic = {i:0 for i in id_list}
    for people in report_dic.values():
        if len(people) != 0:
            for person in people:
                reported_dic[person] += 1
    # print(reported_dic)
    
    # k번 이상 신고받은 사람들 목록 만들기
    lst = []
    for name, num in reported_dic.items():
        if num >= k:
            lst.append(name)
    # print(lst)
    
    # report_dic과 lst 비교해서, 겹치는 숫자만큼 유저 id 순서로 리스트에 담기
    answer = []
    for name, s in report_dic.items():
        cnt = 0
        for each in s:
            if each in lst:
                cnt += 1
        answer.append(cnt)
    
    return answer
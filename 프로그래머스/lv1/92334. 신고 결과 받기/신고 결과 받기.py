def solution(id_list, report, k):
    answer = [0] * len(id_list)
    set_report = set(report)    # 중복 제거
    dic_report = {}     # key: 신고된 사람, value: 신고한 사람 리스트
    count_report = {}   # ket: 신고된 사람, value: 신고된 횟수
    
    # 신고 목록 가져오기
    for rp in set_report:
        reporter, reported = rp.split()     # 문자열에서 신고한 사람, 신고된 사람 분리 
        
        # 딕셔너리에 신고된 사람 추가
        if reported not in dic_report:      # 신고된 사람이 딕셔너리에 없을 경우
            dic_report[reported] = [reporter]
            count_report[reported] = 1
        else:
            dic_report[reported].append(reporter)
            count_report[reported] += 1
    
    # 카운트 딕셔너리에서 꺼내서 신고된 횟수가 k보다 많을 경우 결과 반영
    for reported, count in count_report.items():
        if count >= k:
            for reporter in dic_report[reported]:
                answer[id_list.index(reporter)] += 1
    
    return answer
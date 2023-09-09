def solution(s):
    # 초기 길이는 원래 문자열의 길이로 설정
    answer = len(s)

    # 문자열을 길이의 절반부터 잘라가며 압축을 시도
    for length in range(len(s) // 2, 0, -1):
        count = 1  # 연속으로 같은 문자열이 나타나는 횟수
        sp_b = ""  # 이전 문자열을 저장할 변수
        made_str = ""  # 압축된 문자열을 저장할 변수
        # 문자열 s를 length만큼의 크기로 나눔
        split_s = [s[j:j + length] for j in range(0, len(s), length)]

        # 나눠진 각 문자열 조각에 대해서
        for sp in split_s:
            # 이전 문자열과 같다면, count를 증가
            if sp_b == sp:
                count += 1
            else:
                # 이전 문자열과 다르다면, 만들어질 문자열에 이전 문자열과 횟수를 추가
                if count > 1:
                    made_str += str(count) + sp_b
                else:
                    made_str += sp_b
                sp_b = sp  # 이전 문자열을 현재 문자열로 업데이트
                count = 1  # count를 1로 초기화
            last = sp  # 마지막 문자열 저장

        # 마지막으로 등장한 문자열에 대한 처리
        if count > 1:
            made_str += str(count) + last
        else:
            made_str += last

        # 압축된 문자열의 길이가 더 짧다면, answer를 업데이트
        if answer > len(made_str):
            answer = len(made_str)

    return answer  # 가장 짧게 압축되는 길이를 반환
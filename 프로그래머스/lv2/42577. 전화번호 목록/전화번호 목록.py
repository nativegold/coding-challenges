def solution(phone_book):
    pb_hash = {}
    
    # 딕셔너리를 사용해 해시 만들기
    for pn in phone_book:
        pb_hash[pn] = True
    
    for pn in phone_book:
        finding = ''
        
        # 번호를 하나씩 가져오면서 접두어인 번호 찾기
        for n in pn:
            finding += n
            if finding in pb_hash and finding != pn:
                return False
    
    return True
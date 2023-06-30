def solution(phone_book):
    pb_hash = {}
    
    for pn in phone_book:
        pb_hash[pn] = True
    
    for pn in phone_book:
        finding = ''
        
        for n in pn:
            finding += n
            if finding in pb_hash and finding != pn:
                return False
    
    return True
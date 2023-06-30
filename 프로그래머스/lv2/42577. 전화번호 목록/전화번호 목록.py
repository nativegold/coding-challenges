def solution(phone_book):
    p_dic = {}
    
    for pn in phone_book:
        p_dic[pn] = True
    
    for pn in phone_book:
        finding = ''
        
        for n in pn:
            finding += n
            if finding in p_dic and finding != pn:
                return False
    
    return True
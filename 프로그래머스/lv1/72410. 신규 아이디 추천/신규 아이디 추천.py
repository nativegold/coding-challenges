def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    allowed = '1234567890qwertyuiopasdfghjklzxcvbnm-_.'
    new_id = ''.join([c for c in new_id if c in allowed])  

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계
    if new_id:
        new_id = new_id[1:] if new_id[0] == '.' else new_id
    if new_id:
        new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    
    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
        
    return new_id
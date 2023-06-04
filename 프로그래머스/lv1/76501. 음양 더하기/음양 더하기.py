def solution(absolutes, signs):
    result = 0
    
    for n, sign in zip(absolutes, signs):
        if sign == True:
            result += n
        else:
            result -= n
    
    return result 
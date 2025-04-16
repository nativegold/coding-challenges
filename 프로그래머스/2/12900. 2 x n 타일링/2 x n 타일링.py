def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    way_count_list = [0] * (n + 1)
    way_count_list[1] = 1
    way_count_list[2] = 2
    
    for i in range(3, n + 1):
        way_count_list[i] = ( way_count_list[i - 1] + way_count_list[i - 2] ) % 1000000007
    
    return way_count_list[n]
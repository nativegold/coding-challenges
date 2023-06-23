def solution(array, height):
    taller = [h for h in array if height < h]
    return len(taller)
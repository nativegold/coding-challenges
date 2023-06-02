def solution(arr, divisor):
    li = [n for n in arr if n % divisor == 0]
    li.sort()
    return li if li != [] else [-1]
        
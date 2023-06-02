def solution(arr, divisor):
    arr.sort()
    li = [n for n in arr if n % divisor == 0]
    return li if li != [] else [-1]
        
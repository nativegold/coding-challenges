def solution(price, money, count):
    result = money - sum([price * i for i in range(1, count+1)])
    return 0 if result >= 0 else -result
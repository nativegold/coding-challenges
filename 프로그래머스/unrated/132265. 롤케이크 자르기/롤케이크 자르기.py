from collections import Counter

def solution(toppings):
    answer = 0
    count_topping = Counter(toppings)   
    set_brother = set() 
    
    for topping in toppings:
        count_topping[topping] -= 1
        set_brother.add(topping)
        
        if count_topping[topping] == 0:
            count_topping.pop(topping)
        
        if len(count_topping) == len(set_brother):
            answer += 1
    
    return answer
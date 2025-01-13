
def get_distance(location1, location2):
    x1, y1 = location1
    x2, y2 = location2
    
    return abs(x1 - x2) + abs(y1 - y2)
    

def solution(numbers, hand):
    answer = ''
    numbers = list(map(str, numbers))

    keypad = {
        '*': (3, 0),
        '0': (3, 1),
        '#': (3, 2)
    }
    
    pad_number = 1
    for i in range(3):
        for j in range(3):
            keypad[f'{pad_number}'] = (i, j)
            pad_number += 1
            
    left = '*'
    right = '#'

    for n in numbers:
        if n == '1' or n == '4' or n == '7':
            answer += 'L'
            left = n
        elif n == '3' or n == '6' or n == '9':
            answer += 'R'
            right = n
        elif n == '2' or n == '5' or n == '8' or n == '0':
            left_distance = get_distance(keypad[n], keypad[left])
            right_distance = get_distance(keypad[n], keypad[right])
            
            if left_distance < right_distance:
                answer += 'L'
                left = n
            elif left_distance > right_distance:
                answer += 'R'
                right = n
            elif left_distance == right_distance:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n
    
    return answer
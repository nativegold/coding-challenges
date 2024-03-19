n = int(input())

number = 1
stack = []
operator = []
is_possible = True

for _ in range(n):
    element = int(input())

    while number <= element:
        stack.append(number)
        operator.append("+")
        number += 1

    if stack[-1] == element:
        stack.pop()
        operator.append("-")
    else:
        is_possible = False

if is_possible:
    for op in operator:
        print(op)
else:
    print("NO")
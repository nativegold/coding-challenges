import sys

input = sys.stdin.readline

N = int(input())
b_length_array = []
capacity_before = int(input())
length = 1

for i in range(1, N):
    capacity = int(input())

    if capacity_before != 0 and capacity_before == capacity:
        length += 1
        continue

    b_length_array.append((capacity_before, length))
    capacity_before = capacity
    length = 1

b_length_array.append((capacity_before, length))

max_length = 0

for i in range(len(b_length_array)):
    current_capacity = b_length_array[i][0]
    length = b_length_array[i][1]
    removed_capacity = None

    for j in range(i + 1, len(b_length_array)):
        next_capacity = b_length_array[j][0]
        next_length = b_length_array[j][1]

        if removed_capacity is None:
            removed_capacity = next_capacity
            continue

        if removed_capacity == next_capacity:
            continue

        if removed_capacity != next_capacity and current_capacity != next_capacity:
            break

        length += next_length

    max_length = max(max_length, length)

print(max_length)
disk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = input()

result = 0
before_index = disk.index("A")

for c in letters:
    if abs(disk.index(c) - before_index) < len(disk) - abs(disk.index(c) - before_index):
        result += abs(disk.index(c) - before_index)
    else:
        result += len(disk) - abs(disk.index(c) - before_index)

    before_index = disk.index(c)

print(result)
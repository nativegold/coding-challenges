import sys

readline = sys.stdin.readline
write = sys.stdout.write

X = int(readline())
stick_length = 64
sticks = 1
shortest_stick_length = stick_length

while stick_length != X:
    shortest_stick_length //= 2
    stick_length -= shortest_stick_length

    if stick_length < X:
        stick_length += shortest_stick_length
        sticks += 1

write(f'{sticks}')
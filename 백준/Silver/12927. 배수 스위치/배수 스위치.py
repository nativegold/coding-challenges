electric_bulbs = list(input())
count = 0

while electric_bulbs.count("Y") != 0:
    i = electric_bulbs.index("Y")
    count += 1

    for j in range(i, len(electric_bulbs), i+1):
        electric_bulbs[j] = "N" if electric_bulbs[j] == "Y" else "Y"

print(count)
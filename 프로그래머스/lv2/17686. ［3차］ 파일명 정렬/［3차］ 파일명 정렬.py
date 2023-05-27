def solution(files):
    list_files = []

    for i, file in enumerate(files):
        head = ""
        number = ""
        ended_head = False

        for c in file:
            if c.isdigit():
                number += c
                ended_head = True
            elif not ended_head:
                head += c.upper()
            else:
                break

        list_files.append([head, int(number), i, file])
    list_files.sort()

    return [list_files[i][3] for i in range(len(files))]

def solution(wallpaper):
    start_height = float('inf')
    start_width = float('inf')
    end_height = 0
    end_width = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                start_height = i if i < start_height else start_height
                start_width = j if j < start_width else start_width
                end_height = i+1 if i+1 > end_height else end_height
                end_width = j+1 if j+1 > end_width else end_width

    return [start_height, start_width, end_height, end_width]
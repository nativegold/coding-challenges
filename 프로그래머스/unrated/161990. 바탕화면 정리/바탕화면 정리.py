def solution(wallpaper):
    min_height = float('inf')
    min_width = float('inf')
    max_height = 0
    max_width = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_height = i if i < min_height else min_height
                min_width = j if j < min_width else min_width
                max_height = i+1 if i+1 > max_height else max_height
                max_width = j+1 if j+1 > max_width else max_width
    
    

    return [min_height, min_width, max_height, max_width]
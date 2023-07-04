def solution(sizes):
    width = []
    height = []
    
    for w, h in sizes:
        if w > h:
            width.append(w)
            height.append(h)
        else:
            height.append(w)
            width.append(h)
            
    return max(width) * max(height)
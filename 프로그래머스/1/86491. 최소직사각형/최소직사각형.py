def solution(sizes):

    max_1 = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0],i[1] = i[1],i[0]
        if max_1 < i[0]:
            max_1 = i[0]
    
    max_2 = 0
    for i in sizes:
        if max_2 < i[1]:
            max_2 = i[1]

    return max_1 * max_2
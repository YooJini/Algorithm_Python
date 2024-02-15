def solution(brown, yellow):
    sum = brown + yellow;

    for h in range(1, sum): 
        w = sum // h;
        if (w - 2) * (h - 2) == yellow:
            return [w,h]
    
    
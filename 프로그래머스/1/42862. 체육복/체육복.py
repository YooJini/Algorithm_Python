def solution(n, lost, reserve):
    for i in lost[:]:   # remove시 누락 발생 => 복사본 사용 ([:])
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)

    # 오름차순 정렬
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i-1)
        elif (i + 1) in reserve:
            reserve.remove(i+1)
        else: n = n - 1
    return n
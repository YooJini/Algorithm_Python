from queue import deque
import math

def solution(progresses, speeds):
    answer = []
    # 작업이 끝나기까지 남은 일수
    q = deque()
    for i in range(len(progresses)):
        speed = speeds[i]
        q.append(math.ceil((100-progresses[i]) / speed))

    day = q[0]
    count = 0
    
    while q:
        if day >= q[0]:
            q.popleft()
            count = count + 1
        else:           
            day = q[0]
            answer.append(count)
            count = 0
            
    answer.append(count)
    return answer
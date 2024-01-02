from queue import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)   
    q = deque(people)
    
    while q:
        tmp = q.popleft()
        if q:
            if tmp + q[-1] <= limit:
                q.pop()
        answer = answer + 1
    return answer
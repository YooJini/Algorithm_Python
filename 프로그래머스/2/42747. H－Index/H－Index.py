def solution(citations):
    answer = 0
    citations.sort(reverse = True)
   
    for i in range(len(citations)):
        if citations[i] > answer:
            answer = answer + 1
        else: break
        
    return answer
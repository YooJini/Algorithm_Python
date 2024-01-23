def solution(answers):
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    for idx, ans in enumerate(answers):
        if one[idx%5] == answers[idx]:
            score[0] += 1
        if two[idx%8] == answers[idx]:
            score[1] += 1
        if three[idx%10] == answers[idx]:
            score[2] += 1

    for idx, s in enumerate(score):
        if max(score) == s:
            answer.append(idx+1)
        
    return(answer)
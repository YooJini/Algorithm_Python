# enumerate() 인덱스와 원소로 이루어진 튜플을 만들어 줌
# for 루프를 돌릴 때 인덱스와 원소를 동시에 얻을 수 있음

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
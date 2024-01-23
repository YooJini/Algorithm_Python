def solution(answers):
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = {'1':0,'2':0,'3':0}
    answer = []
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            score['1'] += 1
        if two[i%8] == answers[i]:
            score['2'] += 1
        if three[i%10] == answers[i]:
            score['3'] += 1
  
    score = sorted(score.items(), key=lambda x:x[1], reverse = True)
    max = 0
    for i in score:
        if max <= i[1]:
            answer.append(int(i[0]))
            max = i[1]
        else: break
        
    return(answer)
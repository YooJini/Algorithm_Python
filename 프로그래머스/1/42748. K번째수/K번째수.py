def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        tmp = array[:]
        start = commands[i][0] - 1
        end = commands[i][1]
        tmp = tmp[start:end]
        tmp.sort()
        answer.append(tmp[commands[i][2] - 1])
        
    return answer
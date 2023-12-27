# 배열 자르기 array[startIndex, endIndex] => startIndex ~ endIndex-1
# 오름차순으로 정렬 array.sort() => array가 정렬된 배열로 바뀌므로 다시 넣어줄 필요없음

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
from collections import Counter
def solution(participant, completion):
    dic_p = Counter(participant)
    dic_c = Counter(completion)
    
    return ('').join(list((dic_p - dic_c)))
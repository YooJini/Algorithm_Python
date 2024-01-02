# Counter 사용 (딕셔너리)
# Counter끼리는 덧셈 뺄셈도 가능하다
# dic_p - dic_c => dic_p.subtract(dic_c)
# Counter에 있는 요소들을 list로 변환시켜서 사용

from collections import Counter
def solution(participant, completion):
    dic_p = Counter(participant)
    dic_c = Counter(completion)
    
    return ('').join(list((dic_p - dic_c)))
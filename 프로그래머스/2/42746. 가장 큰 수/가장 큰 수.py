# 문자열은 사전적으로 정렬한다는 것을 이용

def solution(numbers):
    answer = ''
    strs = list(map(str, numbers))
    strs.sort(key = lambda x : x*3, reverse = True)
    # 리스트를 다시 합치는 과정
    # int형으로 받아준다 (ex. 000 => 0)
    # 반환형태는 str
    answer = str(int(''.join(strs)))

    return answer
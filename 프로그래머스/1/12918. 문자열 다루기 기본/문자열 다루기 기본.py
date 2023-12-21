# len(s): 문자열s의 길이
# s.isdigit(): 문자열 s가 숫자형식인지 확인하는 내장함수
# 논리연산자: or, and ... (||, && 아님 주의)
# bool: True, False (첫문자는 대문자로!)
# s.isdigit() == False -> !s.isdigit() 사용안됨 주의

def solution(s):
    answer = True
    
    # s의 길이가 4 혹은 6인지 체크
    # 4도 아니고 6도 아니면 False
    if len(s) != 4 and len(s) != 6:
        answer = False
    
    # 숫자로만 구성되어있는지 체크
    # 그렇지 않다면 False
    if s.isdigit() == False:
        answer = False
        
    return answer
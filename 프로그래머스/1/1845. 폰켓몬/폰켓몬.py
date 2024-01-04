# min(a,b): 더 작은값 구할 때 사용
# set 사용해보기

from collections import Counter

def solution(nums):
    answer = len(nums) / 2
    dic = Counter(nums)
    if len(dic) < answer:
        answer = len(dic)
    return answer
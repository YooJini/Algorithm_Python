from collections import Counter

def solution(nums):
    answer = len(nums) / 2
    dic = Counter(nums)
    if len(dic) < answer:
        answer = len(dic)
    return answer
import sys
input = sys.stdin.readline
result = 0

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)    # 인덱스 1부터 시작하기 위해서 인덱스 0에 0값 넣기
tmp = [0] * (N+1)


def merge_sort(s, e):
    if s == e: return
    m = int(s + (e-s) / 2)
    # 재귀
    merge_sort(s, m)
    merge_sort(m+1, e)
    # tmp에 A복사
    for i in range(s, e+1):
        tmp[i] = A[i]
    # 값 비교 (정렬)
    global result
    k = s    # A배열에서 어느위치에 값이 들어가야하는지 나타내주는 인덱스
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k  # 남아있는 1번 데이터셋에 남아있는 데이터 개수 = swap 횟수
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    # 1번 데이터셋에 데이터가 남아있을 때
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    # 2번 데이터셋에 데이터가 남아있을 때
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


merge_sort(1, N)
print(result)
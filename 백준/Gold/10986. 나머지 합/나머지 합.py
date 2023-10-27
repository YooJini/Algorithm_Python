import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
R = [0] * m

answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    r = S[i] % m
    R[r] += 1
    if r == 0:
        answer += 1

for i in range(m):
    answer += R[i] * (R[i] - 1) // 2

print(answer)
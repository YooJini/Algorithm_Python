N = int(input())
A = list(map(int, input().split()))
S = [0] * N

#삽입정렬
for i in range(1, N):
    insert_index = i
    insert_value = A[i]
    for j in range(i-1, -1, -1): # 앞에 있는 수와 비교
        if A[j] < A[i]:          # 나보다 작으면   
            insert_index = j + 1 # 그 수의 바로 뒤로 들어간다
            break
        if j == 0:               # 끝까지 탐색 마침 => 내가 제일 작은 수
            insert_index = 0     # 인덱스를 맨 앞으로 (0으로)

    for j in range(i, insert_index, -1):
        A[j] = A[j-1]    #오른쪽으로 시프트

    A[insert_index] = insert_value


#합배열
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

result = 0
for i in range(N):
    result += S[i]

print(result)
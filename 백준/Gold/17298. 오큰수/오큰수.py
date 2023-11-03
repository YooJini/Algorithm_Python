n = int(input())
A = list(map(int, input().split()))
ans = [-1] * n
myStack = []

myStack.append(0)

for i in range(1, n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

print(*ans)
from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    
visited_dfs = [0] * (N+1)
visited_bfs = visited_dfs.copy()

def dfs(V):
    visited_dfs[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and graph[V][i] == 1:
            dfs(i)
            
def bfs(V):
    queue = deque()
    queue.append(V)
    visited_bfs[V] = 1
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and graph[V][i] == 1:
                visited_bfs[i] = 1
                queue.append(i)
            
dfs(V)
print()
bfs(V)

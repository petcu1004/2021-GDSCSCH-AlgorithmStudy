from collections import deque

def bfs():
    q = deque()
    q.append((0))
    while q:
        node = q.popleft()
        n = li[node]
        if check[n] == 0 and node != n:
            q.append(n)
            check[n] = check[node] + 1
            if n == K:
                return ;

N, K = map(int, input().split())
li = [int(input()) for _ in range(N)]
check = [0]*N
bfs()
print(check[K] if check[K] else -1)
        
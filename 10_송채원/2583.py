#블록이 몇개인지 알아내기 위한 BFS 너비 우선 탐색 함수를 정의
def bfs(i, j):
    global visited, paper
    
    if paper[i][j] == 1: #직사각형 내부일 경우
        visited.append([i, j])
        return 
    
    block = [] 
    queue = [[i, j]] 
    
    while queue:
        [i, j] = queue.pop(0)
        block.append([i, j]) 
        visited.append([i, j]) #방문 리스트
        
        if paper[i][j] == 0: #상하좌우를 확인하는 조건문
            if i < M-1 and paper[i+1][j] == 0 and [i+1, j] not in block and [i+1, j] not in queue:
                queue.append([i+1, j])
            if j < N-1 and paper[i][j+1] == 0 and [i, j+1] not in block and [i, j+1] not in queue:
                queue.append([i, j+1])
            if i > 0 and paper[i-1][j] == 0 and [i-1, j] not in block and [i-1, j] not in queue:
                queue.append([i-1, j])
            if j > 0 and paper[i][j-1] == 0 and [i, j-1] not in block and [i, j-1] not in queue:
                queue.append([i, j-1])

    return len(block) #블록의 크기 출력


M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1


visited = []
block_list = []

#0,0 부터 M,N까지 각각의 블록
for i in range(M):
    for j in range(N):
        if [i, j] not in visited:
            block = bfs(i, j)
            if block:
                block_list.append(block)


print(len(block_list))
for i in sorted(block_list):
    print(i, end= ' ')
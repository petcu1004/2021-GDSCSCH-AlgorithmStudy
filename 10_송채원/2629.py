import sys
n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
p = []
answer = [[0 for _ in range(15001)] for _ in range(n+1)]

def scale(weight, n, now, left, right):
    new = abs(left-right)
    if new not in p:
        p.append(new)
    if now == n:
        return 0
    if answer[now][new] == 0:
        scale(weight, n, now+1, left+weight[now], right)
        scale(weight, n, now+1, left, right+weight[now])
        scale(weight, n, now+1, left, right)
        answer[now][new] = 1
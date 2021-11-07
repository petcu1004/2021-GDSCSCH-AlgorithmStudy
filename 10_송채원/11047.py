N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]

#코인 총 개수
num = 0

for i in range(1, N+1):
    coin = money[-i]
    if K >= coin:
        m = K//coin
        K -= coin*m
        num += m

print(num)
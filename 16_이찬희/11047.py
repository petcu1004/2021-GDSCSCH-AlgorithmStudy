N, K = map(int,input().split())
Money = [int(input()) for _ in range(N)]

num = 0

for i in range(1, N+1):
    coin = Money[-1]

    if K>=coin:
        n = K // coin
        K -= coin*n
        num += n

print(num)
#브루트 코스
#1부터 n번까지 분해합을 구해서 찾아내기
N = int(input())
small = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))
    result = i + sum(num)
    if result == N:
        print(i)
        break

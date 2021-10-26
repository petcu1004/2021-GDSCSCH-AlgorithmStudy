import sys

n = int(sys.stdin.readline())
res = 1

# 반복문을 통해 1부터 n까지 곱해준다.
for i in range(1, n + 1):
    res *= i

print(res)

import sys

n = int(sys.stdin.readline())

# 반복문을 통해 가장 작은 생성자를 구한다.
for i in range(1, n + 1):
    res = i # 자기 자신

    # 각 자리수의 합
    for j in str(i):
        res += int(j)

    # 현재 수의 분해합이 n과 같다면
    # 현재 수를 출력하고 시스템을 종료 시킨다.
    if res == n:
        print(i)
        exit()

# 반복문이 끝났다면 생성자가 없는 것으로 0을 출력한다.
print(0)

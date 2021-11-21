import sys

weight_num = int(input())
weights = list(map(int, sys.stdin.readline().split()))
bead_num = int(input())
beads = list(map(int, sys.stdin.readline().split()))
result = []
# 이 문제또한 DP로 풀 수 있는 문제
# dp[a][b] 이면 a는 몇 번째인지 b는 무게차이에 대한 값


# 저울이 잴 수 있는 무게는 올려진 추들의 무게 차이



# def doit(weights, weight_num, recent, left, right):
#   possible = abs(left - right)
#   if possible not in result:
#     result.append(possible)
#   if recent == weight_num:
#     return 0
#   # 왼쪽 오른쪽 차이가 없을 경우, 구슬은 왼쪽에 있음
#   if dp[recent][possible] == 0:
#     # 저울 왼쪽 부분 재귀
#     doit(weights, weight_num, recent + 1, left + weights[recent], right)
#     # 저울 오른쪽 부분 재귀
#     doit(weights, weight_num, recent + 1, left, right + weights[recent])
#     # 저울에 아무 것도 안 놓는 재귀
#     doit(weights, weight_num, recent + 1, left, right)
#     dp[recent][possible] = 1
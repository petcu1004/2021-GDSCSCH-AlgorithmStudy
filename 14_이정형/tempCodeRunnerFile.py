# -*- coding:utf-8 -*-
import sys
from collections import Counter

# 몇 개의 수를 받을 건지
num_list = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    num_list.append(num)

# 최빈값 경우로 인해 정렬
num_list.sort()

# 산술평균
print(int(round(sum(num_list) / len(num_list))))
# 중앙값
print(num_list[len(num_list) // 2])
# 최빈값 (최빈수가 여러개일 경우 두 번쨰로 작은 값 출력)
cnt = Counter(num_list).most_common(2)  # 리스트 안 튜플 형태로 저장 감안
if len(num_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[0][0])
    else:
        print(cnt[1][0])
else:
    print(cnt[0][0])
# 범위
print(max(num_list) - min(num_list))

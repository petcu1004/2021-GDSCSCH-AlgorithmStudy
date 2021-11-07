import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(li)/n))

li.sort()
#중앙값
print(li[n//2])

cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

#범위 : 최댓값-최솟값
print(max(li)-min(li))
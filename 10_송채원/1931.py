N = int(input())
li = []
for i in range(N):
    start, end = map(int, input().split())
    li.append((start, end))

li = sorted(li, key=lambda a:a[0])
li = sorted(li, key=lambda a:a[1])

end_time = 0
count = 0
for i in li:
    if i[0] >= end_time:
        end_time = i[1]
        count += 1
print(count)
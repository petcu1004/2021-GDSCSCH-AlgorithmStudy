n = int(input())
num_list = []
for i in range(n):
    a = int(input())
    num_list.append(a)

num_list = sorted(num_list)
num_tuple = tuple(num_list)
print()
print(round(sum(num_list) / n))
print(num_list[int(n / 2)])

max_num = max(num_list)
min_num = min(num_list)
cnt_list = [0] * (max_num - min_num)
for i in num_list:
    cnt_list[i - 1] += 1
print(cnt_list)

save = []
for i in range(len(cnt_list)):
    if cnt_list[i] == max(cnt_list):
        save.append(i + 1)
print(save)
if len(save) > 1:
    print(save[1])
else:
    print(save[0])

print(num_list[-1] - num_list[0])
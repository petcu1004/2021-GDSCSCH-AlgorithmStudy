w = input().upper()
w_list = list(set(w))
count_list = list()

for i in w_list:
    cnt = w.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(w_list[count_list.index(max(count_list))])
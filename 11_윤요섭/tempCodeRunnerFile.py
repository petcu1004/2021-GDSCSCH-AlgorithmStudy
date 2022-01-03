
print(num_1)
print(num_2)
print(num_1 + num_2)

num_sum_list = []
num_sum_list.append(num_0)
num_sum_list.append(num_1)
num_sum_list.append(num_2)
num_sum_list.append(num_3)
num_sum_list.append(num_4)
num_sum_list.append(num_5)
num_sum_list.append(num_6)
num_sum_list.append(num_7)
num_sum_list.append(num_8)
num_sum_list.append(num_9)

for j in range(5):
    for i in range(len(n)):
        x = int(n[i])
        for k in range(3):
            print(num_sum_list[x][j][k], end='')
    print()

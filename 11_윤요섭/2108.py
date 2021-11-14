from collections import Counter
import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    a = int(sys.stdin.readline())
    num_list.append(a)

num_list = sorted(num_list)
num_tuple = tuple(num_list)
#산술평균
print(round(sum(num_list) / n))
#중앙값
print(num_list[int(n / 2)])

max_num = max(num_list)
min_num = min(num_list)
#최빈값 계산
counter = Counter(num_list)
mode = 0  #최빈값
mode_num_1 = min_num  #최빈수중 첫번째로 작은 값
mode_num_2 = 0  #최빈수중 두번째로 작은 값
for i in range(len(num_list)):
    current_num = num_list[i]
    now_counter_num = counter[current_num]
    #현재 카운터 값이 지금까지의 최빈값보다 클때
    if now_counter_num > mode:
        mode = now_counter_num
        mode_num_1 = current_num
        mode_num_2 = ''
    #현재 카운터 값과 지금까지의 최빈값의 크기가 같을때
    elif now_counter_num == mode:
        #mode_num_1과 mode_num_2값이 모두 차있을때
        if mode_num_2 != '':
            #지금 값이 3개의 수중 가장 작을때
            if mode_num_1 > current_num:
                mode_num_2 = mode_num_1
                mode_num_1 = current_num
            #지금 값이 두번째로 작을때
            if mode_num_1 < current_num and current_num < mode_num_2:
                mode_num_2 = current_num
        else:
            #현재 저장된 값이 더 작을때
            if mode_num_1 < current_num:
                mode_num_2 = current_num
            #현재 저장된 값보다 더 작을때
            else:
                mode_num_2 = mode_num_1
                mode_num_1 = current_num

if mode_num_2 == '':
    print(mode_num_1)
else:
    print(mode_num_1)
#범위
print(max_num - min_num)
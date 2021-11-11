from collections import Counter
n = int(input())
num_list = []
for i in range(n):
    a = int(input())
    num_list.append(a)

num_list = sorted(num_list)
num_tuple = tuple(num_list)
#산술평균
print(round(sum(num_list) / n))
#중앙값
print(num_list[int(n / 2)])

max_num = max(num_list)
min_num = min(num_list)
#최빈값
mode = num_list.count(min_num)
mode_list = [mode]
for i in range(len(num_list)):
    mode_list = sorted(mode_list)
    #지금 세고 있는 값의 양이 기존의 최빈값보다 같다면, 최빈값 리스트에 삽입
    if num_list.count(num_list[i]) == mode:
        mode_list.append(num_list[i])
    #지금 세고 있는 값의 양이 기존의 최빈값보다 많다면, 최빈값 리스트를 초기화하고, 해당 값을 리스트에 넣은 다음 최빈값을 해당 값으로 바꿔준다
    elif num_list.count(num_list[i]) > mode:
        mode_list = []
        mode_list.append(num_list[i])
        mode = num_list.count(num_list[i])

if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])
#범위
print(max_num - min_num)
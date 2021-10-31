#수 정렬하기
#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input())
ls = []

#리스트 ls에 N이후로 주어지는 정수를 append하기
for _ in range(N):
    ls.append(int(input()))

#sorted 함수 사용, 오름차순으로 정렬
s = sorted(ls)

#리스트 ls에 정렬된 정수들을 순서대로 출력하기
for i in s:
    print(i)
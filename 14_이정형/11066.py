# -*- coding: utf-8 -*-
import sys

# 테스트 데이터 개수
T = int(input())
# 소설을 구성하는 장의 수
# 1장 부터 K장까지 수록한 파일의 크기
for _ in range(T):
    k = int(input())
    novel = list(map(int, sys.stdin.readline().split()))

    result = [[0] * k for _ in range(k)]

print(result)

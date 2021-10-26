# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:00:00 2021

@author: Geonwoo Ji
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        rt = n * factorial(n-1)
        return rt

n = int(input())

print(factorial(n))

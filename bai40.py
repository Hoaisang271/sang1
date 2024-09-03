#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:40:12 2024

@author: hoaisangduong
"""

def tinh_S40(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / (2 * i)
    return S

n = int(input("Nhập n cho bài 40: "))
print(f"Kết quả bài 40: S({n}) =", tinh_S40(n))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:42:37 2024

@author: hoaisangduong
"""

def tinh_S44(n):
    S = 0
    for i in range(1, n + 1):
        S += (2 * i - 1) / (2 * i)
    return S

n = int(input("Nhập n cho bài 44: "))
print(f"Kết quả bài 44: S({n}) =", tinh_S44(n))

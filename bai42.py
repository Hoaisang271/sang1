#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:41:18 2024

@author: hoaisangduong
"""

def tinh_S42(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / (i * (i + 1))
    return S

n = int(input("Nhập n cho bài 42: "))
print(f"Kết quả bài 42: S({n}) =", tinh_S42(n))
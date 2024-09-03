#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:43:20 2024

@author: hoaisangduong
"""

def tinh_S45(n, x):
    S = x
    for i in range(2, n + 1):
        denom = sum(range(1, i + 1))
        S += (x ** i) / denom
    return S

n = int(input("Nhập n cho bài 45: "))
x = float(input("Nhập x cho bài 45: "))
print(f"Kết quả bài 45: S({n}, {x}) =", tinh_S45(n, x))
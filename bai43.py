#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:41:56 2024

@author: hoaisangduong
"""

def tinh_S43(n):
    S = 0
    for i in range(1, n + 1):
        S += i / (i + 1)
    return S

n = int(input("Nhập n cho bài 43: "))
print(f"Kết quả bài 43: S({n}) =", tinh_S43(n))
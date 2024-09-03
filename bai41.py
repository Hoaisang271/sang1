#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:40:46 2024

@author: hoaisangduong
"""

def tinh_S41(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / (2 * i + 1)
    return S

n = int(input("Nhập n cho bài 41: "))
print(f"Kết quả bài 41: S({n}) =", tinh_S41(n))

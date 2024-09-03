#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:39:25 2024

@author: hoaisangduong
"""


def tinh_S39(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    return S

n = int(input("Nhập n cho bài 39: "))
print(f"Kết quả bài 39: S({n}) =", tinh_S39(n))

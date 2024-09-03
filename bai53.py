#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:12:54 2024

@author: hoaisangduong
"""

def tong_n(n):
    return n * (n + 1) // 2  # Sử dụng công thức tổng của dãy số

n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng S = 1 + 2 + ... + {n} là: {tong_n(n)}")

def tong_binh_phuong_n(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng S = 1^2 + 2^2 + ... + {n}^2 là: {tong_binh_phuong_n(n)}")

def tong_nghich_dao_n(n):
    return sum(1 / i for i in range(1, n + 1))

n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng S = 1 + 1/2 + ... + 1/{n} là: {tong_nghich_dao_n(n)}")

import math

def tong_giai_thua_n(n):
    return sum(math.factorial(i) for i in range(1, n + 1))

n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng S = 1! + 2! + ... + {n}! là: {tong_giai_thua_n(n)}")

def tich_n(n):
    return math.prod(range(1, n + 1))

n = int(input("Nhập số nguyên dương n: "))
print(f"Tích S = 1 * 2 * ... * {n} là: {tich_n(n)}")
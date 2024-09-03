#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:48:12 2024

@author: hoaisangduong
"""
import math

def can_bac_x(n, x):
    return n ** (1 / x)

# Nhập số nguyên dương n và bậc x
n = int(input("Nhập số nguyên dương n: "))
x = int(input("Nhập bậc x: "))
print(f"Căn bậc {x} của {n} là: {can_bac_x(n, x)}")
def so_dao(n):
    return int(str(n)[::-1])

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"Số đảo của {n} là: {so_dao(n)}")

def la_so_chinh_phuong(n):
    return int(math.sqrt(n)) ** 2 == n

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"{n} có phải là số chính phương: {la_so_chinh_phuong(n)}")
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"{n} có phải là số nguyên tố: {la_so_nguyen_to(n)}")

def tich_cac_chu_so_le(n):
    tich = 1
    has_odd = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            tich *= int(digit)
            has_odd = True
    return tich if has_odd else 0  # Nếu không có chữ số lẻ thì trả về 0

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"Tích các chữ số lẻ của {n} là: {tich_cac_chu_so_le(n)}")
def tong_so_nguyen_to_nho_hon(n):
    tong = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong += i
    return tong

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_so_nguyen_to_nho_hon(n)}")

def tong_so_chinh_phuong_nho_hon(n):
    tong = 0
    for i in range(1, n):
        if la_so_chinh_phuong(i):
            tong += i
    return tong

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng các số chính phương nhỏ hơn {n} là: {tong_so_chinh_phuong_nho_hon(n)}")
def tong_uoc_so_duong(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng các ước số dương của {n} là: {tong_uoc_so_duong(n)}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:08:44 2024

@author: hoaisangduong
"""

while True:
    try:
        N = int(input("Nhập vào số nguyên dương N: "))
        if N > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Đây không phải là số nguyên. Vui lòng nhập lại.")

tong = sum(int(chu_so) for chu_so in str(N))

print(f"Tổng các chữ số của {N} là: {tong}")
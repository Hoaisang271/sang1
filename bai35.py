#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:21:36 2024

@author: hoaisangduong
"""
while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

S = sum(range(1, n + 1))
print(f"Tổng S = 1 + 2 + 3 + ... + {n} = {S}")
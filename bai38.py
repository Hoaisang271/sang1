#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:28:05 2024

@author: hoaisangduong
"""

while True:
    try:
        n = int(input("Nhập vào số nguyên dương lẻ n: "))
        if n > 0 and n % 2 != 0:
            break
        else:
            print("Vui lòng nhập một số nguyên lẻ lớn hơn 0.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

S = 1
for i in range(1, n + 1):
    S *= i
print(f"Tích S = 1 * 2 * 3 * ... * {n} = {S}")
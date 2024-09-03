#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:18:11 2024

@author: hoaisangduong
"""

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
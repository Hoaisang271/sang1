#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:19:46 2024

@author: hoaisangduong
"""

import math
def la_so_chinh_phuong(n):
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n
while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if la_so_chinh_phuong(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
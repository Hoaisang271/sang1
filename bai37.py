#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:27:02 2024

@author: hoaisangduong
"""
while True:
    try:
        n = int(input("Nhập vào số nguyên dương chẵn n: "))
        if n > 0 and n % 2 == 0:
            break
        else:
            print("Vui lòng nhập một số nguyên chẵn lớn hơn 0.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
S = sum(i for i in range(2, n + 1, 2))

print(f"Tổng S = 2 + 4 + 6 + ... + {n} = {S}")
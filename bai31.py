#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:07:29 2024

@author: hoaisangduong
"""

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

while True:
    try:
        a = int(input("Nhập cạnh a: "))
        b = int(input("Nhập cạnh b: "))
        c = int(input("Nhập cạnh c: "))
        
        if a > 0 and b > 0 and c > 0:
            break
        else:
            print("Vui lòng nhập ba số nguyên dương.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if la_tam_giac(a, b, c):
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba cạnh này không lập thành tam giác.")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:09:48 2024

@author: hoaisangduong
"""
while True:
    try:
        so_km = float(input("Nhập vào số km đã đi: "))
        if so_km > 0:
            break
        else:
            print("Số km phải lớn hơn 0. Vui lòng nhập lại.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if so_km <= 1:
    tien_cuoc = 15000
elif 1 < so_km <= 5:
    tien_cuoc = 15000 + (so_km - 1) * 13500
elif 5 < so_km <= 120:
    tien_cuoc = 15000 + 4 * 13500 + (so_km - 5) * 11000
else:
    tien_cuoc = 15000 + 4 * 13500 + (120 - 5) * 11000 + (so_km - 120) * 11000
    tien_cuoc *= 0.9  

print(f"Số tiền cước taxi là: {tien_cuoc} VND")
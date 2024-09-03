#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:06:27 2024

@author: hoaisangduong
"""
def la_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    return False

while True:
    try:
        thang = int(input("Nhập vào tháng (1-12): "))
        nam = int(input("Nhập vào năm: "))
        
        if thang < 1 or thang > 12:
            print("Tháng không hợp lệ. Vui lòng nhập lại.")
        else:
            break
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if thang in [1, 3, 5, 7, 8, 10, 12]:
    ngay = 31
elif thang in [4, 6, 9, 11]:
    ngay = 30
elif thang == 2:
    if la_nam_nhuan(nam):
        ngay = 29
    else:
        ngay = 28

print(f"Tháng {thang} năm {nam} có {ngay} ngày.")
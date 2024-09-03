#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:44:39 2024

@author: hoaisangduong
"""

def kiem_tra_doan():
    while True:
        try:
            n = float(input("Nhập vào một giá trị: "))
            if -89 <= n <= 90:
                print(f"Giá trị {n} nằm trong đoạn [-89, 90].")
                break
            else:
                print(f"Giá trị {n} không nằm trong đoạn [-89, 90]. Vui lòng nhập lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
                        
kiem_tra_doan()
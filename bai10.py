#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:48:58 2024

@author: hoaisangduong
"""

def tinh_so_nut(bien_so):
    tong = sum(int(chu_so) for chu_so in str(bien_so))
    while tong >= 10:
        tong = sum(int(chu_so) for chu_so in str(tong))
    return tong

bien_so = input("Nhập biển số xe của bạn (4 chữ số): ")
print(f"Số nút của biển số xe {bien_so} là: {tinh_so_nut(bien_so)}")
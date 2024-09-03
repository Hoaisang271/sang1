#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:16:35 2024

@author: hoaisangduong
"""

def chu_vi_hcn(dai, rong):
    return 2 * (dai + rong)

dai = int(input("Nhập chiều dài: "))
rong = int(input("Nhập chiều rộng: "))
print(f"Chu vi của hình chữ nhật là: {chu_vi_hcn(dai, rong)}")

def dien_tich_hcn(dai, rong):
    return dai * rong

print(f"Diện tích của hình chữ nhật là: {dien_tich_hcn(dai, rong)}")

def ve_hinh_chu_nhat(dai, rong):
    for i in range(rong):
        print('*' * dai)

ve_hinh_chu_nhat(dai, rong)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:43:36 2024

@author: hoaisangduong
"""
def kiem_tra_so(n):
    if n < 0 and n % 2 != 0:
        return -1 
    elif n > 0 and n % 2 == 0:
        return 1 
    else:
        return 0  
n = int(input("Nhập một số: "))

ket_qua = kiem_tra_so(n)
print(f"Kết quả kiểm tra số {n} là: {ket_qua}")
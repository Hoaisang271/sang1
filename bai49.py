#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:40:13 2024

@author: hoaisangduong
"""
def kiem_tra_chan_am(n):
    return n % 2 == 0 and n < 0
n = int(input("Nhập một số: "))
if kiem_tra_chan_am(n):
    print(f"{n} là số chẵn và có giá trị âm: True")
else:
    print(f"{n} không phải là số chẵn âm: False")
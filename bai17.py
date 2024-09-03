#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:21:54 2024

@author: hoaisangduong
"""
def find_max_min(num1, num2, num3):
    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)
    
    return max_num, min_num
try:
    num1 = int(input("Nhập số nguyên thứ nhất: "))
    num2 = int(input("Nhập số nguyên thứ hai: "))
    num3 = int(input("Nhập số nguyên thứ ba: "))
    
    largest, smallest = find_max_min(num1, num2, num3)
    
    print(f"Số lớn nhất là: {largest}")
    print(f"Số nhỏ nhất là: {smallest}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")


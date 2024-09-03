#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:02:52 2024

@author: hoaisangduong
"""
def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    
    return largest
try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))

    largest = find_largest(a, b, c)
    
    print(f"Số lớn nhất là: {largest}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")

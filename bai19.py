#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:44:05 2024

@author: hoaisangduong
"""
def find_smallest(a, b, c, d):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    
    return smallest

try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    d = int(input("Nhập số nguyên d: "))
  
    smallest = find_smallest(a, b, c, d)
    
    print(f"Số nhỏ nhất là: {smallest}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")

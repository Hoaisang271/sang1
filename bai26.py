#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:06:08 2024

@author: hoaisangduong
"""

def sort_three_numbers(a, b, c):

    temp = a
    
    if a > b:
        temp = a
        a = b
        b = temp
    
    if a > c:
        temp = a
        a = c
        c = temp
    
    if b > c:
        temp = b
        b = c
        c = temp
    
    return a, b, c

try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    c = int(input("Nhập số c: "))
    
    sorted_a, sorted_b, sorted_c = sort_three_numbers(a, b, c)
    print(f"Các số theo thứ tự tăng dần: {sorted_a}, {sorted_b}, {sorted_c}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")
    
    
def sort_digits(n):
    sorted_digits = ''.join(sorted(str(n)))
    return sorted_digits

try:
    n = int(input("Nhập số nguyên N: "))
    
    sorted_number = sort_digits(n)
    print(f"Số có các chữ số theo thứ tự tăng dần là: {sorted_number}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:04:45 2024

@author: hoaisangduong
"""

def toggle_case(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()
    else:
        return char
char = input("Nhập một chữ cái: ")
if len(char) == 1 and char.isalpha():
    result = toggle_case(char)
    print(f"Ký tự sau khi đổi là: {result}")
else:
    print("Vui lòng nhập đúng một chữ cái.")

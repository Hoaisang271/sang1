#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:11:23 2024

@author: hoaisangduong
"""

def is_valid_time(giờ, phút, giây):
    if 0 <= giờ <= 23 and 0 <= phút <= 59 and 0 <= giây <= 59:
        return True
    return False
try:
    giờ = int(input("Nhập giờ (0-23): "))
    phút = int(input("Nhập phút (0-59): "))
    giây = int(input("Nhập giây (0-59): "))
    if is_valid_time(giờ, phút, giây):
        print("Thời gian hợp lệ.")
    else:
        print("Thời gian không hợp lệ.")
except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")

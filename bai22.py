#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:06:44 2024

@author: hoaisangduong
"""

print("Giai phuong trinh bac nhat: ax+b=0 ")
a = float(input("nhap a:"))
b = float(input(" nhap b: "))
if a == 0 and b != 0:
    print("Phuong trinh vo nghiem")
elif a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem")    
else:
    print("Nghiem cua phuong trinh la: ", -b/a )
    
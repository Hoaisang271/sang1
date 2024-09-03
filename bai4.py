#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:27:24 2024

@author: hoaisangduong
"""
N = int(input("Nhap so nguyen duong N co 2 chu so: "))
if N < 10 or N > 99:
    print("So nhap vao khong phai la hai so nguyen duong co 2 chu so.")
else:
    a = N //10
    b = N % 10
    s = a + b
    print( f" {a} + {b} = {s}")
    
 

       
    

    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:57:18 2024

@author: hoaisangduong
"""


x=int(input('Nhập vào số giây:'));
gio = x//3600;
x=x%3600;
phut=x//60;
x=x%60;
print('Kết quả =', gio,'giờ :', phut, 'phút :', x,'giây');
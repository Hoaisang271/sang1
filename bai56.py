#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:17:48 2024

@author: hoaisangduong
"""
import math

def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh', None)
    tinh = kwargs.get('tinh', None)
    
    if hinh == 'vuong':
        canh = args[0]
        if tinh == 'cv':
            return 4 * canh  
        elif tinh == 'dt':
            return canh ** 2  
        else:
            return "Phép tính không hợp lệ!"
    
    elif hinh == 'chu_nhat':
        dai = args[0]
        rong = args[1]
        if tinh == 'cv':
            return 2 * (dai + rong) 
        elif tinh == 'dt':
            return dai * rong 
        else:
            return "Phép tính không hợp lệ!"
    
    elif hinh == 'tron':
        ban_kinh = args[0]
        if tinh == 'cv':
            return 2 * math.pi * ban_kinh  
        elif tinh == 'dt':
            return math.pi * ban_kinh ** 2  
        else:
            return "Phép tính không hợp lệ!"
    
    else:
        return "Hình không hợp lệ!"

# Các ví dụ gọi hàm theo yêu cầu
print(tinh(10, hinh='vuong', tinh='cv'))   
print(tinh(50, hinh='vuong', tinh='dt'))    
print(tinh(18, hinh='tron', tinh='cv'))     
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))  
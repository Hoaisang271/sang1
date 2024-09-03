#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:29:28 2024

@author: hoaisangduong
"""
for x in range(1, 980 // 2):
    for y in range(1, (980 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) // 9
        if 2 * x + 7 * y + 9 * z == 979 and z > 0:
            print(f"Bộ nghiệm (x, y, z) = ({x}, {y}, {z})")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:37:55 2024

@author: hoaisangduong
"""
max_sum = 0
best_solution = None

for x in range(1, 980 // 2):
    for y in range(1, (980 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) // 9
        if 2 * x + 7 * y + 9 * z == 979 and z > 0:
            if x + y + z > max_sum:
                max_sum = x + y + z
                best_solution = (x, y, z)

if best_solution:
    print(f"Bộ nghiệm (x, y, z) lớn nhất: {best_solution} với tổng {max_sum}")
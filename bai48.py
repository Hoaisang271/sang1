#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:39:09 2024

@author: hoaisangduong
"""
min_sum = float('inf')
best_solution = None

for x in range(1, 980 // 2):
    for y in range(1, (980 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) // 9
        if 2 * x + 7 * y + 9 * z == 979 and z > 0:
            if x + y + z < min_sum:
                min_sum = x + y + z
                best_solution = (x, y, z)

if best_solution:
    print(f"Bộ nghiệm (x, y, z) nhỏ nhất: {best_solution} với tổng {min_sum}")
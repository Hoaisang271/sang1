#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:15:45 2024

@author: hoaisangduong
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Nhập số phần tử của dãy Fibonacci: "))
print(f"{n} phần tử đầu tiên của dãy Fibonacci là: {fibonacci(n)}")

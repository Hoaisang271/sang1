#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:53:21 2024

@author: hoaisangduong
"""

def format_date(day, month, year, format_type):
    """Định dạng ngày tháng năm theo kiểu được yêu cầu."""
    if format_type == 'a':
        return f"{day}/{month}/{year}"
    elif format_type == 'b':
        # Rút ngắn năm về hai chữ số
        return f"{day}/{month}/{year % 100}"
    elif format_type == 'c':
        return f"{year}/{month}/{day}"
    else:
        return "Định dạng không hợp lệ."

def parse_date(date_str, format_type):
    """Chuyển đổi định dạng ngày tháng năm về định dạng gốc."""
    if format_type == 'a':
        day, month, year = map(int, date_str.split('/'))
        return day, month, year
    elif format_type == 'b':
        day, month, year = date_str.split('/')
        return int(day), int(month), int(year) + 1900  # Giả sử năm là 1900 + 2 chữ số cuối
    elif format_type == 'c':
        year, month, day = map(int, date_str.split('/'))
        return day, month, year
    else:
        return None
try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    print("Chọn định dạng xuất (a: Ngày/tháng/năm, b: Ngày/tháng/năm (rút ngắn năm), c: Năm/tháng/ngày): ")
    format_type = input().strip().lower()
    formatted_date = format_date(day, month, year, format_type)
    print(f"Ngày tháng năm theo định dạng {format_type} là: {formatted_date}")
    print(f"\nNhập ngày tháng năm theo định dạng {format_type} để chuyển đổi ngược lại:")
    date_str = input("Nhập ngày tháng năm: ")
    original_date = parse_date(date_str, format_type)
    
    if original_date:
        print(f"Ngày tháng năm gốc là: {original_date[0]}/{original_date[1]}/{original_date[2]}")
    else:
        print("Định dạng ngày tháng năm không hợp lệ.")

except ValueError:
    print("Vui lòng nhập đúng định dạng số nguyên.")

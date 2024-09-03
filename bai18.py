#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:02:26 2024

@author: hoaisangduong
"""

def time_to_seconds(hours, minutes, seconds):
    """Chuyển đổi giờ, phút, giây thành tổng số giây."""
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(total_seconds):
    """Chuyển đổi tổng số giây thành giờ, phút, giây."""
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def main():
    # Nhập thời gian thứ nhất
    print("Nhập thời gian thứ nhất:")
    h1 = int(input("Giờ: "))
    m1 = int(input("Phút: "))
    s1 = int(input("Giây: "))

    # Nhập thời gian thứ hai
    print("Nhập thời gian thứ hai:")
    h2 = int(input("Giờ: "))
    m2 = int(input("Phút: "))
    s2 = int(input("Giây: "))

    # Chuyển đổi thời gian thành giây
    time1_seconds = time_to_seconds(h1, m1, s1)
    time2_seconds = time_to_seconds(h2, m2, s2)

    # Cộng và trừ thời gian
    sum_seconds = time1_seconds + time2_seconds
    diff_seconds = abs(time1_seconds - time2_seconds)  # Sử dụng giá trị tuyệt đối cho phép trừ

    # Chuyển đổi kết quả về giờ, phút, giây
    sum_time = seconds_to_time(sum_seconds)
    diff_time = seconds_to_time(diff_seconds)

    # In kết quả
    print(f"Tổng thời gian: {sum_time[0]} giờ {sum_time[1]} phút {sum_time[2]} giây")
    print(f"Hiệu thời gian: {diff_time[0]} giờ {diff_time[1]} phút {diff_time[2]} giây")

if __name__ == "__main__":
    main()

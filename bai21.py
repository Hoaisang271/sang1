#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:17:03 2024

@author: hoaisangduong
"""

def number_to_word(number):
    """Chuyển số nguyên từ 0 đến 9 thành chuỗi tương ứng bằng tiếng Việt."""
    words = {
        0: "Khong",
        1: "Mot",
        2: "Hai",
        3: "Ba",
        4: "Bon",
        5: "Nam",
        6: "Sau",
        7: "Bay",
        8: "Tam",
        9: "Chin"
    }
    return words.get(number, "Khong doc duoc")

def main():
    try:
        number = int(input("Nhap 1 so bat ky: "))
        # Kiểm tra nếu số nằm trong khoảng từ 0 đến 9
        if 0 <= number <= 9:
            print(number_to_word(number))
        else:
            print("Khong doc duoc")
    except ValueError:
        print("Vui long nhap mot so nguyen.")

if __name__ == "__main__":
    main()

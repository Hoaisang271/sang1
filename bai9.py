#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:06:53 2024

@author: hoaisangduong
"""

def in_menu():
    print("============ MENU ============")
    print("1. Hu tieu")
    print("2. Chao long")
    print("3. Banh canh")
    print("4. Bun rieu")
    print("5. Pho bo")
    print("==============================")
    lua_chon = input("Moi nhap lua chon: ")
    return lua_chon
lua_chon = in_menu()
print(f"Ban da chon: {lua_chon}")

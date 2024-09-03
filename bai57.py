#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:23:13 2024

@author: hoaisangduong
"""

import random

class SinhVien:
    def __init__(self, ma_sv, ho_ten, gpa):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gpa = gpa
        self.xep_loai = self.cap_nhat_xep_loai()

    def cap_nhat_xep_loai(self):
        if self.gpa < 3.5:
            return "Kém"
        elif 3.5 <= self.gpa < 5.0:
            return "Yếu"
        elif 5.0 <= self.gpa < 7.0:
            return "Trung bình"
        elif 7.0 <= self.gpa < 8.0:
            return "Khá"
        elif 8.0 <= self.gpa < 9.0:
            return "Giỏi"
        elif 9.0 <= self.gpa <= 10.0:
            return "Xuất sắc"
        return "Không hợp lệ"

    def in_thong_tin(self):
        print(f"Mã SV: {self.ma_sv}, Họ tên: {self.ho_ten}, GPA: {self.gpa:.2f}, Xếp loại: {self.xep_loai}")


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []

    def khoi_tao_sv_tu_danh_sach(self, danh_sach_sv):
        for sv in danh_sach_sv:
            self.danh_sach_sv.append(SinhVien(sv['ma_sv'], sv['ho_ten'], sv['gpa']))

    def khoi_tao_sv_ngau_nhien(self, so_luong):
        ho_ten_mau = ["Nguyen Van A", "Le Thi B", "Tran Van C", "Hoang Thi D", "Pham Van E"]
        for _ in range(so_luong):
            ma_sv = f"SV{random.randint(1000, 9999)}"
            ho_ten = random.choice(ho_ten_mau)
            gpa = round(random.uniform(0, 10), 2)
            self.danh_sach_sv.append(SinhVien(ma_sv, ho_ten, gpa))

    def in_danh_sach_sv(self):
        for sv in self.danh_sach_sv:
            sv.in_thong_tin()

    def tim_sv_diem_cao_nhat(self):
        if not self.danh_sach_sv:
            print("Không có sinh viên nào.")
            return
        sv_diem_cao_nhat = max(self.danh_sach_sv, key=lambda sv: sv.gpa)
        print("Sinh viên có điểm trung bình cao nhất:")
        sv_diem_cao_nhat.in_thong_tin()

    def tim_sv_theo_ma(self, ma_sv):
        for sv in self.danh_sach_sv:
            if sv.ma_sv == ma_sv:
                return sv
        return None

    def tim_sv_theo_gpa(self, gpa):
        return [sv for sv in self.danh_sach_sv if sv.gpa == gpa]

    def top_10_sv_gpa_cao_nhat(self):
        sorted_sv = sorted(self.danh_sach_sv, key=lambda sv: sv.gpa, reverse=True)
        return sorted_sv[:10]

    def top_10_sv_gpa_thap_nhat(self):
        sorted_sv = sorted(self.danh_sach_sv, key=lambda sv: sv.gpa)
        return sorted_sv[:10]


# Khởi tạo đối tượng quản lý sinh viên
quan_ly_sv = QuanLySinhVien()

# Khởi tạo sinh viên từ danh sách có sẵn
danh_sach_sv_ban_dau = [
    {"ma_sv": "SV1001", "ho_ten": "Nguyen Van A", "gpa": 7.5},
    {"ma_sv": "SV1002", "ho_ten": "Le Thi B", "gpa": 6.5},
    {"ma_sv": "SV1003", "ho_ten": "Tran Van C", "gpa": 9.0},
]
quan_ly_sv.khoi_tao_sv_tu_danh_sach(danh_sach_sv_ban_dau)

# Khởi tạo thêm sinh viên ngẫu nhiên
quan_ly_sv.khoi_tao_sv_ngau_nhien(5)

# Xuất thông tin tất cả sinh viên
quan_ly_sv.in_danh_sach_sv()
# Xuất sinh viên có điểm trung bình cao nhất
quan_ly_sv.tim_sv_diem_cao_nhat()

# Tìm sinh viên theo mã sinh viên
ma_sv_can_tim = "SV1002"
sv_tim_thay = quan_ly_sv.tim_sv_theo_ma(ma_sv_can_tim)
if sv_tim_thay:
    print(f"Sinh viên tìm thấy với mã {ma_sv_can_tim}:")
    sv_tim_thay.in_thong_tin()
else:
    print(f"Không tìm thấy sinh viên với mã {ma_sv_can_tim}.")

# Tìm sinh viên theo điểm trung bình
gpa_can_tim = 7.5
sv_theo_gpa = quan_ly_sv.tim_sv_theo_gpa(gpa_can_tim)
if sv_theo_gpa:
    print(f"Sinh viên có GPA {gpa_can_tim}:")
    for sv in sv_theo_gpa:
        sv.in_thong_tin()
else:
    print(f"Không tìm thấy sinh viên có GPA {gpa_can_tim}.")

# Top 10 sinh viên có GPA cao nhất
print("Top 10 sinh viên có GPA cao nhất:")
for sv in quan_ly_sv.top_10_sv_gpa_cao_nhat():
    sv.in_thong_tin()

# Top 10 sinh viên có GPA thấp nhất
print("Top 10 sinh viên có GPA thấp nhất:")
for sv in quan_ly_sv.top_10_sv_gpa_thap_nhat():
    sv.in_thong_tin()
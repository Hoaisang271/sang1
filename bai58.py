#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:25:16 2024

@author: hoaisangduong
"""

import random

# Lớp cha cơ bản cho nhân viên
class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_co_ban):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban

    def tinh_luong_hang_thang(self):
        pass

    def in_thong_tin(self):
        print(f"Mã NV: {self.ma_nv}, Họ tên: {self.ho_ten}, Lương cơ bản: {self.luong_co_ban}đ, Lương hằng tháng: {self.tinh_luong_hang_thang()}đ")


# Lớp cho nhân viên văn phòng
class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_ngay_lam_viec):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_ngay_lam_viec = so_ngay_lam_viec

    def tinh_luong_hang_thang(self):
        return self.luong_co_ban + self.so_ngay_lam_viec * 150_000


# Lớp cho nhân viên bán hàng
class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_san_pham):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_san_pham = so_san_pham

    def tinh_luong_hang_thang(self):
        return self.luong_co_ban + self.so_san_pham * 18_000


class CongTy:
    def __init__(self, so_luong_nv=300):
        self.so_luong_nv = so_luong_nv
        self.danh_sach_nv = []

    def khoi_tao_ngau_nhien(self):
        ho_ten_mau = ["Nguyen Van A", "Le Thi B", "Tran Van C", "Hoang Thi D", "Pham Van E"]
        for i in range(self.so_luong_nv):
            ma_nv = f"NV{i + 1:03}"
            ho_ten = random.choice(ho_ten_mau)
            luong_co_ban = random.randint(3_000_000, 8_000_000)
            if random.choice([True, False]):
                so_ngay_lam_viec = random.randint(20, 26)
                nhan_vien = NhanVienVanPhong(ma_nv, ho_ten, luong_co_ban, so_ngay_lam_viec)
            else:
                so_san_pham = random.randint(50, 200)
                nhan_vien = NhanVienBanHang(ma_nv, ho_ten, luong_co_ban, so_san_pham)
            self.danh_sach_nv.append(nhan_vien)

    def in_danh_sach_nv(self):
        for nv in self.danh_sach_nv:
            nv.in_thong_tin()

    def tim_nv_theo_ma(self, ma_nv):
        for nv in self.danh_sach_nv:
            if nv.ma_nv == ma_nv:
                return nv
        return None

    def tim_nv_luong_cao_nhat(self):
        if not self.danh_sach_nv:
            return None
        return max(self.danh_sach_nv, key=lambda nv: nv.tinh_luong_hang_thang())

    def tim_nv_ban_hang_luong_thap_nhat(self):
        nv_ban_hang = [nv for nv in self.danh_sach_nv if isinstance(nv, NhanVienBanHang)]
        if not nv_ban_hang:
            return None
        return min(nv_ban_hang, key=lambda nv: nv.tinh_luong_hang_thang())


# Khởi tạo công ty với 10 nhân viên để dễ kiểm tra (có thể đổi thành 300)
cong_ty = CongTy(10)
cong_ty.khoi_tao_ngau_nhien()

# In danh sách tất cả nhân viên
print("Danh sách nhân viên:")
cong_ty.in_danh_sach_nv()

# Tìm nhân viên theo mã
ma_nv_can_tim = "NV005"

nv_tim_thay = cong_ty.tim_nv_theo_ma(ma_nv_can_tim)
if nv_tim_thay:
    print(f"\nNhân viên tìm thấy với mã {ma_nv_can_tim}:")
    nv_tim_thay.in_thong_tin()
else:
    print(f"\nKhông tìm thấy nhân viên với mã {ma_nv_can_tim}.")

# Tìm nhân viên có lương hằng tháng cao nhất
nv_luong_cao_nhat = cong_ty.tim_nv_luong_cao_nhat()
if nv_luong_cao_nhat:
    print("\nNhân viên có lương hằng tháng cao nhất:")
    nv_luong_cao_nhat.in_thong_tin()

# Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
nv_ban_hang_thap_nhat = cong_ty.tim_nv_ban_hang_luong_thap_nhat()
if nv_ban_hang_thap_nhat:
    print("\nNhân viên bán hàng có lương hằng tháng thấp nhất:")
    nv_ban_hang_thap_nhat.in_thong_tin()
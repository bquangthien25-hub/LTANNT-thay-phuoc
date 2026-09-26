so_gio_lam = float(input("Nhap so gio lam moi tuan: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần
gio_thuong = min(so_gio_lam, gio_tieu_chuan)   # Số giờ làm trong mức chuẩn
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)  # Số giờ làm vượt chuẩn
thuc_linh = gio_thuong * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"So tien thuc linh cua nhan vien: {thuc_linh}")
import os

def ghi_hoa_don_txt(so_phong, noi_dung):
    # Tạo thư mục nếu chưa có
    if not os.path.exists("Hoa_Don_Output"):
        os.makedirs("Hoa_Don_Output")
    
    ten_file = f"Hoa_Don_Output/Phong_{so_phong}.txt"
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print(f"📄 Đã in hóa đơn phòng {so_phong}")
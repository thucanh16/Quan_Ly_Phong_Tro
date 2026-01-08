def create_invoice(r_id, e, w):
    """Hàm in hóa đơn dựa trên mã phòng, số điện và số nước"""
    print("\n" + "="*30)
    print(f"   HÓA ĐƠN PHÒNG: {r_id}")
    print("="*30)
    
    # Tính toán tiền (Giá giả định)
    tien_dien = e * 3500
    tien_nuoc = w * 10000
    tong_cong = tien_dien + tien_nuoc
    
    print(f"⚡ Tiền điện ({e} số): {tien_dien:,} VND")
    print(f"💧 Tiền nước ({w} khối): {tien_nuoc:,} VND")
    print("-" * 30)
    print(f"💰 TỔNG CỘNG: {tong_cong:,} VND")
    print("="*30)
    print("✅ In hóa đơn thành công!")
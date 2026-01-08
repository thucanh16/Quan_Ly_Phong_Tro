import json
import os
from config import INVOICES_FILE

def load_history():
    """Chức năng 6: Lấy dữ liệu lịch sử từ file JSON"""
    if not os.path.exists(INVOICES_FILE):
        return []
    try:
        with open(INVOICES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_invoice(r_id, room_price, electric, water):
    """Chức năng 4: Tính tổng, Lưu JSON và Xuất bản in .txt"""
    total = room_price + electric + water
    invoice_data = {
        "room_id": r_id,
        "total": total,
        "details": {"room": room_price, "electric": electric, "water": water}
    }
    
    # Lưu vào lịch sử hệ thống để tính doanh thu
    history = load_history()
    history.append(invoice_data)
    with open(INVOICES_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
    
    # Xuất file text (HoaDon_Phong_xxx.txt) như bạn thấy trong VS Code
    file_name = f"HoaDon_Phong_{r_id}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"===== HÓA ĐƠN PHÒNG {r_id} =====\n")
        f.write(f"Tiền phòng: {room_price:,} VND\n")
        f.write(f"Tiền điện:  {electric:,} VND\n")
        f.write(f"Tiền nước:  {water:,} VND\n")
        f.write(f"---------------------------\n")
        f.write(f"TỔNG CỘNG:  {total:,} VND\n")
    return total
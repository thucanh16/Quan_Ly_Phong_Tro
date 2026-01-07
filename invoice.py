from data_handler import load_data, save_data
from datetime import datetime
import json

ROOM_PATH = "data/rooms.json"
TENANT_PATH = "data/tenants.json"
INVOICE_PATH = "data/invoices.json"
SERVICE_PATH = "data/services.json"

def create_invoice(room_id, dien_moi, dien_cu):
    # Load tất cả dữ liệu cần thiết
    rooms = load_data(ROOM_PATH)
    tenants = load_data(TENANT_PATH)
    invoices = load_data(INVOICE_PATH)
    
    # Đọc giá dịch vụ từ services.json
    try:
        with open(SERVICE_PATH, 'r', encoding='utf-8') as f:
            services = json.load(f)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file services.json!")
        return

    # 1. Kiểm tra phòng tồn tại
    room = next((r for r in rooms if r["room_id"] == room_id), None)
    if room is None:
        print(f"Lỗi: Phòng {room_id} không tồn tại!")
        return

    # 2. Kiểm tra khách thuê
    tenant = next((t for t in tenants if t["room_id"] == room_id), None)
    if tenant is None:
        print(f"Phòng {room_id} chưa có người ở!")
        return

    # 3. Tính toán các chi phí từ services.json
    tien_phong = room["price"]
    
    # Tiền điện = (Số mới - Số cũ) * Giá điện
    so_dien_tieu_thu = dien_moi - dien_cu
    tien_dien = so_dien_tieu_thu * services["electricity"]
    
    # Các chi phí cố định
    tien_nuoc = services["water"]
    tien_net = services["internet"]
    tien_rac = services["garbage"]
    
    tong_cong = tien_phong + tien_dien + tien_nuoc + tien_net + tien_rac

    # 4. Lưu hóa đơn
    new_invoice = {
        "room_id": room_id,
        "tenant": tenant["name"],
        "details": {
            "room_price": tien_phong,
            "electricity": tien_dien,
            "water": tien_nuoc,
            "internet": tien_net,
            "garbage": tien_rac
        },
        "total_amount": tong_cong,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    invoices.append(new_invoice)
    save_data(INVOICE_PATH, invoices)

    # 5. In kết quả ra màn hình cực đẹp
    print("\n" + "="*40)
    print(f"      HÓA ĐƠN PHÒNG {room_id}")
    print("="*40)
    print(f"Khách thuê: {tenant['name']}")
    print(f"- Tiền phòng:  {tien_phong:>15,} VNĐ")
    print(f"- Tiền điện:   {tien_dien:>15,} VNĐ ({so_dien_tieu_thu} kWh)")
    print(f"- Tiền nước:   {tien_nuoc:>15,} VNĐ")
    print(f"- Internet:    {tien_net:>15,} VNĐ")
    print(f"- Phí rác:     {tien_rac:>15,} VNĐ")
    print("-" * 40)
    print(f"TỔNG CỘNG:     {tong_cong:>15,} VNĐ")
    print("="*40)
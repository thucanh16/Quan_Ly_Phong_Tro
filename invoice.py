from data_handler import load_data, save_data
from datetime import datetime
import json
from reporting import export_invoice_to_txt # Kết nối báo cáo

ROOM_PATH = "data/rooms.json"
TENANT_PATH = "data/tenants.json"
INVOICE_PATH = "data/invoices.json"
SERVICE_PATH = "data/services.json"

def create_invoice(room_id, dien_moi, dien_cu):
    rooms = load_data(ROOM_PATH)
    tenants = load_data(TENANT_PATH)
    invoices = load_data(INVOICE_PATH)
    
    try:
        with open(SERVICE_PATH, 'r', encoding='utf-8') as f:
            services = json.load(f)
    except FileNotFoundError:
        print("Lỗi: Không thấy services.json!")
        return

    room = next((r for r in rooms if r["room_id"] == room_id), None)
    tenant = next((t for t in tenants if t["room_id"] == room_id), None)

    if not room or not tenant:
        print("Lỗi: Phòng trống hoặc không tồn tại!")
        return

    # Tính toán
    tien_dien = (dien_moi - dien_cu) * services["electricity"]
    tong_cong = room["price"] + tien_dien + services["water"] + services["internet"] + services["garbage"]

    # Lưu dữ liệu
    new_invoice = {
        "room_id": room_id,
        "tenant": tenant["name"],
        "details": {
            "room_price": room["price"],
            "electricity": tien_dien,
            "water": services["water"],
            "internet": services["internet"],
            "garbage": services["garbage"]
        },
        "total_amount": tong_cong,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    invoices.append(new_invoice)
    save_data(INVOICE_PATH, invoices)
    
    # GỌI XUẤT FILE TXT
    export_invoice_to_txt(new_invoice)

    print(f"\n--- ĐÃ TÍNH XONG PHÒNG {room_id} ---")
    print(f"Tổng tiền: {tong_cong:,} VNĐ")
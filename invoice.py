from data_handler import load_data, save_data
from datetime import datetime
import json
from reporting import export_invoice_to_txt # Đã thêm đúng nhánh Báo cáo

ROOM_PATH = "data/rooms.json"
TENANT_PATH = "data/tenants.json"
INVOICE_PATH = "data/invoices.json"
SERVICE_PATH = "data/services.json"

def create_invoice(room_id, dien_moi, dien_cu):
    # Load dữ liệu
    rooms = load_data(ROOM_PATH)
    tenants = load_data(TENANT_PATH)
    invoices = load_data(INVOICE_PATH)
    
    # Đọc giá dịch vụ
    try:
        with open(SERVICE_PATH, 'r', encoding='utf-8') as f:
            services = json.load(f)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file services.json!")
        return

    # 1. Kiểm tra phòng và khách
    room = next((r for r in rooms if r["room_id"] == room_id), None)
    tenant = next((t for t in tenants if t["room_id"] == room_id), None)

    if room is None or tenant is None:
        print(f"Lỗi: Kiểm tra lại số phòng {room_id} hoặc khách thuê!")
        return

    # 2. Tính toán chi phí
    tien_phong = room["price"]
    so_dien_tieu_thu = dien_moi - dien_cu
    tien_dien = so_dien_tieu_thu * services["electricity"]
    
    tong_cong = tien_phong + tien_dien + services["water"] + services["internet"] + services["garbage"]

    # 3. Tạo đối tượng hóa đơn
    new_invoice = {
        "room_id": room_id,
        "tenant": tenant["name"],
        "details": {
            "room_price": tien_phong,
            "electricity": tien_dien,
            "water": services["water"],
            "internet": services["internet"],
            "garbage": services["garbage"]
        },
        "total_amount": tong_cong,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    # 4. Lưu vào JSON và Xuất file TXT (Chỉ gọi 1 lần duy nhất)
    invoices.append(new_invoice)
    save_data(INVOICE_PATH, invoices)
    export_invoice_to_txt(new_invoice) # Kết nối nhánh Reporting

    # 5. In kết quả đẹp mắt
    print("\n" + "="*40)
    print(f"      HÓA ĐƠN PHÒNG {room_id}")
    print("="*40)
    print(f"Khách thuê: {tenant['name']}")
    print(f"- Tiền phòng:  {tien_phong:>15,} VNĐ")
    print(f"- Tiền điện:   {tien_dien:>15,} VNĐ ({so_dien_tieu_thu} kWh)")
    print(f"- Tổng cộng:   {tong_cong:>15,} VNĐ")
    print("="*40)
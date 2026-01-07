<<<<<<< HEAD
import datetime
from config import INVOICES_FILE, INVOICE_UNPAID
=======
import os
import json
>>>>>>> 9ca8312 (hoan thien chuc nang in hoa don)
from data_handler import load_data, save_data
# Dòng này để kết nối với file printer.py bạn vừa tạo
from printer import ghi_hoa_don_txt

<<<<<<< HEAD
class Invoice:
    def __init__(self, room_number, customer_name, items):
        self.room_number = room_number
        self.customer_name = customer_name
        self.items = items # [{name, price, quantity}]
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def save_to_db(self):
        invoices = load_data(INVOICES_FILE)
        new_data = {
            "room_number": self.room_number,
            "customer": self.customer_name,
            "date": self.date,
            "total": self.calculate_total(),
            "status": INVOICE_UNPAID
        }
        invoices.append(new_data)
        save_data(INVOICES_FILE, invoices)
=======
def create_invoice(room_id, electricity, water):
    rooms = load_data("data/rooms.json")
    room = next((r for r in rooms if str(r.get('id')) == str(room_id)), None)

    if room:
        try:
            price = room.get('price', 0)
            total = price + (electricity * 3500) + (water * 15000)
            
            # Lưu lịch sử
            history = load_data("data/history.json")
            history.append({"room_id": room_id, "total": total, "date": "08/01/2026"})
            save_data("data/history.json", history)

            # 1. In thông báo ra màn hình đen (Terminal)
            print(f"✅ Thành công! Tổng tiền: {total:,} VNĐ")
            
            # 2. GỌI LỆNH IN RA FILE (Dòng này sẽ tạo thư mục Hoa_Don_Output)
            noidung = f"Hoa don phong: {room_id}\nTong tien: {total:,} VND"
            ghi_hoa_don_txt(room_id, noidung)

        except Exception as e:
            print(f"❌ Lỗi: {e}")
    else:
        print(f"❌ Không tìm thấy phòng!")
>>>>>>> 9ca8312 (hoan thien chuc nang in hoa don)

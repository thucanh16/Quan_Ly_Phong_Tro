import os
import json

# --- CẤU HÌNH DỮ LIỆU ---
DATA_DIR = "data"
ROOMS_FILE = os.path.join(DATA_DIR, "rooms.json")
INVOICES_FILE = os.path.join(DATA_DIR, "invoices.json")

# Tự động tạo thư mục và file nếu chưa có để tránh lỗi
if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)

def load_db(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try: return json.load(f)
            except: return []
    return []

def save_db(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- PHẦN XỬ LÝ 7 CHỨC NĂNG ---

def xem_danh_sach(): # Chức năng 1
    rooms = load_db(ROOMS_FILE)
    print("\n" + "="*30 + "\n[1] DANH SÁCH PHÒNG")
    if not rooms: print("Chưa có phòng nào.")
    for r in rooms:
        print(f"Phòng {r['id']} | Giá: {r['price']:,} | Khách: {r['tenant']} | TT: {r['status']}")

def them_phong(): # Chức năng 2
    rooms = load_db(ROOMS_FILE)
    rid = input("Nhập số phòng mới: ")
    try:
        price = int(input("Nhập giá thuê: "))
        rooms.append({"id": rid, "price": price, "status": "Trống", "tenant": "Chưa có"})
        save_db(ROOMS_FILE, rooms)
        print(f"✅ Đã thêm phòng {rid}!")
    except: print("❌ Lỗi: Giá tiền phải là số!")

def them_khach(): # Chức năng 3
    rooms = load_db(ROOMS_FILE)
    rid = input("Nhập số phòng cần thêm khách: ")
    for r in rooms:
        if r['id'] == rid:
            r['tenant'] = input("Tên khách thuê: ")
            r['status'] = "Đã thuê"
            save_db(ROOMS_FILE, rooms)
            print(f"✅ Đã cập nhật khách cho phòng {rid}")
            return
    print("❌ Không tìm thấy phòng!")

def tao_hoa_don(): # Chức năng 4
    rooms = load_db(ROOMS_FILE)
    rid = input("Lập hóa đơn cho phòng: ")
    # Tìm phòng để lấy giá gốc tự động
    room = next((r for r in rooms if r['id'] == rid), None)
    
    try:
        p_room = room['price'] if room else int(input("Không thấy giá gốc, nhập giá phòng: "))
        e = int(input("Tiền điện: "))
        w = int(input("Tiền nước: "))
        total = p_room + e + w
        
        # Lưu vào lịch sử (Chức năng 6 & 7)
        invs = load_db(INVOICES_FILE)
        invs.append({"room_id": rid, "total": total})
        save_db(INVOICES_FILE, invs)
        
        # Xuất file text hóa đơn
        with open(f"HoaDon_Phong_{rid}.txt", "w", encoding="utf-8") as f:
            f.write(f"HOA DON PHONG {rid}\n----------------\nTong: {total:,} VND")
        print(f"✅ Xong! Tổng tiền: {total:,} VND (Đã xuất file .txt)")
    except Exception as err:
        print(f"❌ Lỗi: {err}")

def tim_kiem(): # Chức năng 5
    rid = input("Nhập số phòng cần tìm: ")
    rooms = load_db(ROOMS_FILE)
    for r in rooms:
        if r['id'] == rid:
            print(f"🔍 Kết quả: Phòng {r['id']}, Giá {r['price']:,}, Khách {r['tenant']}")
            return
    print("❌ Không thấy phòng này.")

def lich_su(): # Chức năng 6
    print("\n[6] LỊCH SỬ HÓA ĐƠN")
    for h in load_db(INVOICES_FILE):
        print(f"Phòng {h['room_id']}: {h['total']:,} VND")

def doanh_thu(): # Chức năng 7
    history = load_db(INVOICES_FILE)
    total = sum(h['total'] for h in history)
    print(f"\n📊 TỔNG DOANH THU HỆ THỐNG: {total:,} VND")

# --- ĐIỀU KHIỂN CHƯƠNG TRÌNH ---
def main():
    while True:
        print("\n" + "="*35)
        print("   QUẢN LÝ PHÒNG TRỌ (7 CHỨC NĂNG)")
        print("="*35)
        print("1. Xem phòng  | 2. Thêm phòng | 3. Thêm khách")
        print("4. Hóa đơn    | 5. Tìm kiếm   | 6. Lịch sử")
        print("7. Doanh thu  | 0. Thoát")
        
        chon = input("\nChọn chức năng: ")
        if chon == "1": xem_danh_sach()
        elif chon == "2": them_phong()
        elif chon == "3": them_khach()
        elif chon == "4": tao_hoa_don()
        elif chon == "5": tim_kiem()
        elif chon == "6": lich_su()
        elif chon == "7": doanh_thu()
        elif chon == "0": break
        else: print("❌ Vui lòng chọn từ 0-7!")

if __name__ == "__main__":
    main()
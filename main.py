import room
import tenant
import invoice
import json
import os

# Hàm này bắt buộc phải có để mục số 6 hoạt động
def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def main():
    while True:
        print("\n" + "="*30)
        print("   QUẢN LÝ PHÒNG TRỌ")
        print("="*30)
        print("1. Xem danh sách phòng")
        print("2. Thêm phòng mới")
        print("3. Thêm khách thuê")
        print("4. Tạo hóa đơn (In & Lưu)")
        print("5. Tìm kiếm phòng")
        print("6. Xem lịch sử hóa đơn")
        print("0. Thoát")
        
        choice = input("Chọn chức năng: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            room.view_rooms()
        elif choice == "2":
            room.add_room()
        elif choice == "3":
            tenant.add_tenant_to_room()
        elif choice == "4":
            r_id = input("Mã phòng: ")
            d_str = input("Chỉ số điện: ")
            n_str = input("Chỉ số nước: ")
            
            if d_str.isdigit() and n_str.isdigit():
                # Gọi hàm từ invoice.py mà bạn vừa sửa lúc nãy
                invoice.create_invoice(r_id, int(d_str), int(n_str))
            else:
                print("❌ Lỗi: Điện và nước phải nhập số!")
                
        elif choice == "5":
            room.find_room()
        elif choice == "6":
            # Đọc file từ thư mục data bạn đã tạo
            history = load_data("data/history.json")
            print("\n--- LỊCH SỬ HÓA ĐƠN ---")
            if not history:
                print("Chưa có dữ liệu lịch sử.")
            else:
                for h in history:
                    print(h)
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
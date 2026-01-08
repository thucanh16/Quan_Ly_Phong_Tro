import room
import tenant
import invoice
import json
import os

def load_data(file_path):
    """Hàm đọc dữ liệu từ file JSON an toàn"""
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
        print("   HỆ THỐNG QUẢN LÝ PHÒNG TRỌ")
        print("="*30)
        print("1. Xem danh sách phòng")
        print("2. Thêm phòng mới")
        print("3. Thêm khách thuê vào phòng")
        print("4. Tạo hóa đơn (In hóa đơn)")
        print("5. Tìm kiếm phòng")
        print("6. Xem lịch sử hóa đơn")
        print("0. Thoát chương trình")
        print("-" * 30)
        
        choice = input("Mời bạn chọn chức năng (0-6): ").strip()

        if choice == "0":
            print("👋 Cảm ơn bạn đã sử dụng phần mềm. Tạm biệt!")
            break
            
        elif choice == "1":
            room.view_rooms()
            
        elif choice == "2":
            room.add_room()
            
        elif choice == "3":
            tenant.add_tenant_to_room()
            
        elif choice == "4":
            r_id = input("Nhập mã phòng cần in hóa đơn: ").strip()
            d_str = input("Nhập chỉ số điện mới: ").strip()
            n_str = input("Nhập chỉ số nước mới: ").strip()
            
            # Kiểm tra kỹ thuật: Chỉ khi cả 2 là số thì mới gọi hàm
            if d_str.isdigit() and n_str.isdigit():
                e = int(d_str)
                w = int(n_str)
                # Gọi hàm từ invoice.py với 3 tham số
                invoice.create_invoice(r_id, e, w)
            else:
                print("❌ Lỗi: Chỉ số điện và nước bắt buộc phải nhập số!")
                
        elif choice == "5":
            room.find_room()
            
        elif choice == "6":
            history = load_data("data/history.json")
            print("\n--- LỊCH SỬ GIAO DỊCH/HÓA ĐƠN ---")
            if not history:
                print("Chưa có lịch sử nào được ghi lại.")
            else:
                for idx, h in enumerate(history, 1):
                    print(f"{idx}. {h}")
        
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn lại từ 0 đến 6.")

if __name__ == "__main__":
    main()
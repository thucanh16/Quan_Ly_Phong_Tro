import room, tenant, invoice
from data_handler import load_data

def main():
    while True:
        print("\n" + "="*25 + "\n1. Xem phòng\n2. Thêm phòng\n3. Thêm khách\n4. Lập hóa đơn\n5. Tìm phòng\n6. Lịch sử\n0. Thoát\n" + "="*25)
        choice = input("Chọn: ")

        if choice == "1": room.view_rooms()
        elif choice == "2": room.add_room()
        elif choice == "3": tenant.add_tenant_to_room()
        elif choice == "4":
            r_id = input("Mã phòng: ")
            try:
                e = int(input("Chỉ số điện: "))
                w = int(input("Chỉ số nước: "))
                invoice.create_invoice(r_id, e, w)
            except: print("❌ Vui lòng nhập số!")
        elif choice == "5": room.find_room()
        elif choice == "6":
            history = load_data("data/history.json")
            print("\n--- LỊCH SỬ ---")
            for h in history:
                print(f"Phòng: {h.get('room_id')} | Tiền: {h.get('total_amount', 0):,} | Ngày: {h.get('date')}")
        elif choice == "0": break
        else: print("❌ Chọn sai!")

if __name__ == "__main__":
    main()
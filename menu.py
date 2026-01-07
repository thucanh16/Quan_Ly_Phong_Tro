import menu
import room
import tenant
import invoice
import reporting

def main():
    while True:
        menu.show_main_menu()
        choice = input("Chọn chức năng (0-4): ")

        if choice == "1":
            handle_room_sub_menu()
        elif choice == "2":
            handle_tenant_sub_menu()
        elif choice == "3":
            handle_invoice_sub_menu()
        elif choice == "4":
            handle_report_sub_menu()
        elif choice == "0":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Ví dụ hàm xử lý menu con cho Phòng
def handle_room_sub_menu():
    while True:
        menu.room_menu()
        choice = input("Chọn chức năng: ")
        if choice == "1":
            # Gọi logic từ room.py
            rid = input("Nhập mã phòng: ")
            price = int(input("Nhập giá: "))
            room.add_room(rid, price)
        elif choice == "2":
            rooms = room.list_rooms()
            for r in rooms: print(r)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
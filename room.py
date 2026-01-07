from data_handler import load_data, save_data

def view_rooms():
    rooms = load_data("data/rooms.json")
    if not rooms:
        print("\n📭 Danh sách phòng trống.")
        return
    print("\n--- DANH SÁCH PHÒNG ---")
    for r in rooms:
        status = r.get('status', 'Trống')
        print(f"Phòng: {r.get('id')} | Giá: {r.get('price', 0):,} VNĐ | {status}")

def add_room():
    rooms = load_data("data/rooms.json")
    r_id = input("Nhập mã phòng mới: ")
    if any(r.get('id') == r_id for r in rooms):
        print("❌ Mã phòng đã tồn tại!")
        return
    try:
        price = int(input("Nhập giá thuê: "))
        rooms.append({"id": r_id, "price": price, "status": "Trống"})
        save_data("data/rooms.json", rooms)
        print("✅ Thêm phòng thành công!")
    except:
        print("❌ Giá phòng phải là số!")

def find_room():
    # CHỨC NĂNG XEM LỊCH SỬ (MƯỢN PHÍM SỐ 5)
    history = load_data("data/history.json")
    print("\n" + "="*30)
    print("   LỊCH SỬ THANH TOÁN")
    print("="*30)
    if not history:
        print("Chưa có lịch sử nào.")
    else:
        for h in history:
            print(f"Phòng: {h.get('room_id')} | Tiền: {h.get('total', 0):,} VNĐ | Ngày: {h.get('date')}")
    print("="*30)

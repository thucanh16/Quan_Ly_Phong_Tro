from data_handler import load_data, save_data

def add_tenant_to_room():
    rooms = load_data("data/rooms.json")
    r_id = input("Nhập mã phòng khách thuê: ")
    room = next((r for r in rooms if str(r.get('id')) == r_id), None)
    
    if room:
        if room.get('status') == "Đã thuê":
            print("⚠️ Phòng này đã có người ở!")
            return
        name = input("Nhập tên khách thuê: ")
        room['tenant'] = name
        room['status'] = "Đã thuê"
        save_data("data/rooms.json", rooms)
        print(f"✅ Đã thêm khách {name} vào phòng {r_id}")
    else:
        print("❌ Mã phòng không tồn tại!")
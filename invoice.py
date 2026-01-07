from data_handler import load_data, save_data

def create_invoice(room_id, electricity, water):
    # Đảm bảo đọc đúng file
    rooms = load_data("data/rooms.json")
    
    # Tìm phòng - Chú ý ép kiểu str để so sánh chính xác
    room = next((r for r in rooms if str(r.get('id')) == str(room_id)), None)
    
    if room:
        try:
            # Tính toán tiền bạc
            price = room.get('price', 0)
            total = price + (electricity * 3500) + (water * 15000)
            
            new_inv = {
                "room_id": room_id,
                "total": total,
                "date": "07/01/2026"
            }
            
            # Lưu vào lịch sử
            history = load_data("data/history.json")
            history.append(new_inv)
            save_data("data/history.json", history)
            
            print(f"✅ Thành công! Tổng tiền: {total:,} VNĐ")
        except Exception as e:
            print(f"❌ Lỗi tính toán: {e}")
    else:
        print(f"❌ Không tìm thấy phòng mã {room_id}!")
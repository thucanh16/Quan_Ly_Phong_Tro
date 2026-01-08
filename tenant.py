# Import để sử dụng hằng số, giúp tránh lỗi gõ sai chữ "Đã thuê" hoặc "Trống"
from config import ROOMS_FILE, ROOM_OCCUPIED, ROOM_EMPTY
from data_handler import load_data, save_data

def add_tenant_to_room():
    # Sử dụng ROOMS_FILE thay vì ghi đường dẫn cứng
    rooms = load_data(ROOMS_FILE)
    r_id = input("Nhập mã phòng khách thuê: ")
    
    # Tìm phòng dựa trên ID (đã ép kiểu string để so sánh chính xác)
    room = next((r for r in rooms if str(r.get('id')) == r_id), None)
    
    if room:
        # Sử dụng hằng số ROOM_OCCUPIED ("Đã thuê") từ config
        if room.get('status') == ROOM_OCCUPIED:
            print("⚠️ Cảnh báo: Phòng này hiện đã có người ở!")
            return
            
        name = input("Nhập tên khách thuê: ")
        # Cập nhật thông tin khách và trạng thái phòng
        room['tenant'] = name
        room['status'] = ROOM_OCCUPIED # Sử dụng biến hằng số
        
        # Lưu lại vào file JSON thông qua data_handler
        save_data(ROOMS_FILE, rooms)
        print(f"✅ Thành công: Đã thêm khách {name} vào phòng {r_id}")
    else:
        print("❌ Lỗi: Mã phòng không tồn tại trên hệ thống!")
        
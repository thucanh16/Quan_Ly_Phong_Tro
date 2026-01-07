# Import các hằng số từ config để đồng bộ 100% với dự án
from config import ROOMS_FILE, HISTORY_FILE, ROOM_EMPTY, ROOM_OCCUPIED
from data_handler import load_data, save_data

def view_rooms():
    # Sử dụng ROOMS_FILE thay vì ghi "data/rooms.json"
    rooms = load_data(ROOMS_FILE)
    if not rooms:
        print("\n📭 Danh sách phòng hiện đang trống dữ liệu.")
        return
    
    print("\n--- DANH SÁCH PHÒNG ---")
    for r in rooms:
        # Sử dụng hằng số ROOM_EMPTY làm mặc định nếu không có trạng thái
        status = r.get('status', ROOM_EMPTY)
        # Định dạng tiền tệ chuyên nghiệp cho đồ án
        print(f"Phòng: {r.get('id')} | Giá: {r.get('price', 0):,} VNĐ | Trạng thái: {status}")

def add_room():
    rooms = load_data(ROOMS_FILE)
    r_id = input("Nhập mã phòng mới: ")
    
    # Kiểm tra trùng lặp để bảo vệ tính toàn vẹn của dữ liệu
    if any(r.get('id') == r_id for r in rooms):
        print("❌ Lỗi: Mã phòng này đã tồn tại trên hệ thống!")
        return
    
    try:
        price = int(input("Nhập giá thuê hàng tháng: "))
        # Khởi tạo phòng mới với trạng thái ROOM_EMPTY từ config
        rooms.append({"id": r_id, "price": price, "status": ROOM_EMPTY})
        save_data(ROOMS_FILE, rooms)
        print(f"✅ Thành công: Đã thêm phòng {r_id} vào danh sách!")
    except ValueError:
        print("❌ Lỗi: Giá phòng phải là một con số nguyên!")

def view_payment_history():
    # Sử dụng HISTORY_FILE để đồng bộ với cấu trúc thư mục data
    history = load_data(HISTORY_FILE)
    print("\n" + "="*40)
    print("      LỊCH SỬ THANH TOÁN")
    print("="*40)
    
    if not history:
        print("Hệ thống chưa ghi nhận lịch sử thanh toán nào.")
    else:
        for h in history:
            # Hiển thị lịch sử lấy từ history.json
            print(f"Phòng: {h.get('room_id')} | Tổng tiền: {h.get('total', 0):,} VNĐ | Ngày: {h.get('date')}")
    print("="*40)
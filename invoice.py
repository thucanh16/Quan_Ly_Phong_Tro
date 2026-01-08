import json

def create_invoice(r_id, e, w):
    # 1. Tính tiền (Giữ nguyên logic cũ của bạn)
    tong = (e * 3500) + (w * 10000)
    
    # 2. In kết quả ra màn hình
    print(f"\n✅ ĐÃ TẠO HÓA ĐƠN PHÒNG {r_id}")
    print(f"Tổng tiền: {tong:,} VND")

    # 3. LƯU LỊCH SỬ (Phần thêm mới)
    file_path = "data/history.json"
    try:
        # Đọc dữ liệu cũ từ file
        with open(file_path, "r", encoding="utf-8") as f:
            history = json.load(f)
    except:
        history = []

    # Viết thêm dòng mới vào danh sách
    history.append(f"Phòng {r_id}: Điện {e}, Nước {w} -> Tổng {tong:,} VND")

    # Ghi lại danh sách mới vào file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
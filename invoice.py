def create_invoice():
    room_id = input("Mã phòng: ").strip()
    
    try:
        # Sử dụng .strip() để xóa mọi dấu cách thừa và ép kiểu trực tiếp
        dien_moi = int(input("Chỉ số điện: ").strip())
        nuoc_moi = int(input("Chỉ số nước: ").strip())
        
        # Nếu chạy đến đây tức là đã nhập số thành công
        print(f"\n✅ Đã nhận: Điện {dien_moi}, Nước {nuoc_moi}")
        # Thực hiện tính toán tiếp ở đây...
        
    except ValueError:
        # Nếu người dùng nhập chữ hoặc để trống, Python sẽ nhảy vào đây
        print("❌ Vui lòng nhập số!")
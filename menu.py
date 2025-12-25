# menu.py

def show_main_menu():
    print("\n" + "=" * 40)
    print("      HỆ THỐNG QUẢN LÝ PHÒNG TRỌ")
    print("=" * 40)
    print("1. Quản lý phòng")
    print("2. Quản lý người thuê")
    print("3. Lập hóa đơn")
    print("4. Báo cáo - thống kê")
    print("0. Thoát")
    print("=" * 40)


def room_menu():
    print("\n--- QUẢN LÝ PHÒNG ---")
    print("1. Thêm phòng")
    print("2. Danh sách phòng")
    print("3. Cập nhật phòng")
    print("4. Xóa phòng")
    print("0. Quay lại")


def tenant_menu():
    print("\n--- QUẢN LÝ NGƯỜI THUÊ ---")
    print("1. Thêm người thuê")
    print("2. Danh sách người thuê")
    print("3. Cập nhật người thuê")
    print("4. Xóa người thuê")
    print("0. Quay lại")


def invoice_menu():
    print("\n--- QUẢN LÝ HÓA ĐƠN ---")
    print("1. Lập hóa đơn")
    print("2. Danh sách hóa đơn")
    print("3. Thanh toán hóa đơn")
    print("0. Quay lại")


def report_menu():
    print("\n--- BÁO CÁO - THỐNG KÊ ---")
    print("1. Doanh thu theo tháng")
    print("2. Phòng còn trống")
    print("3. Phòng chưa thanh toán")
    print("0. Quay lại")


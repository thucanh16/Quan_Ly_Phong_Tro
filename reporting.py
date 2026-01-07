from config import INVOICES_FILE, ROOMS_FILE, ROOM_EMPTY
from data_handler import load_data

def get_monthly_revenue(month, year):
    """Tính tổng doanh thu thực tế từ các hóa đơn đã thanh toán trong tháng."""
    all_invoices = load_data(INVOICES_FILE)
    total = 0
    count = 0
    
    for inv in all_invoices:
        # Giả sử ngày lưu dạng 'dd-mm-yyyy'
        inv_date = inv['date'].split(' ')[0]
        d, m, y = inv_date.split('-')
        
        if m == month and y == year:
            total += inv['total']
            count += 1
            
    return total, count

def list_unpaid_invoices():
    """Liệt kê các hóa đơn chưa thanh toán để chủ trọ nhắc nhở khách."""
    all_invoices = load_data(INVOICES_FILE)
    return [inv for inv in all_invoices if inv['status'] == "Chưa thanh toán"]

def get_room_occupancy():
    """Báo cáo tỷ lệ lấp đầy phòng."""
    rooms = load_data(ROOMS_FILE)
    total_rooms = len(rooms)
    empty_rooms = len([r for r in rooms if r['status'] == ROOM_EMPTY])
    
    return {
        "total": total_rooms,
        "occupied": total_rooms - empty_rooms,
        "empty": empty_rooms
    }
import os
from datetime import datetime

def export_invoice_to_txt(invoice_data):
    # 1. Tạo thư mục 'exports' nếu chưa có
    if not os.path.exists('exports'):
        os.makedirs('exports')

    # 2. Đặt tên file (Ví dụ: HoaDon_Phong_101_07012026.txt)
    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    file_name = f"exports/HoaDon_Phong_{invoice_data['room_id']}_{timestamp}.txt"

    # 3. Nội dung hóa đơn trình bày đẹp
    content = f"""
========================================
       HÓA ĐƠN TIỀN PHÒNG TRỌ
========================================
Ngày xuất: {invoice_data['date']}
Phòng: {invoice_data['room_id']}
Khách thuê: {invoice_data['tenant']}
----------------------------------------
CHI TIẾT DỊCH VỤ:
- Tiền phòng:      {invoice_data['details']['room_price']:,} VNĐ
- Tiền điện:       {invoice_data['details']['electricity']:,} VNĐ
- Tiền nước:       {invoice_data['details']['water']:,} VNĐ
- Internet:        {invoice_data['details']['internet']:,} VNĐ
- Phí rác:         {invoice_data['details']['garbage']:,} VNĐ
----------------------------------------
TỔNG CỘNG:         {invoice_data['total_amount']:,} VNĐ
========================================
      Cảm ơn quý khách đã thuê phòng!
========================================
"""
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Đã xuất hóa đơn: {file_name}")
    except Exception as e:
        print(f"❌ Lỗi xuất file: {e}")
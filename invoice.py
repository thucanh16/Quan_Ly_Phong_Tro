import datetime

class Invoice:
    def __init__(self, customer_name, items):
        """
        Khởi tạo hóa đơn
        :param customer_name: Tên khách hàng
        :param items: Danh sách các món đồ (mỗi món là một dict: {'name': str, 'price': float, 'quantity': int})
        """
        self.customer_name = customer_name
        self.items = items
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def calculate_total(self):
        """Tính tổng tiền hóa đơn"""
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def display_invoice(self):
        """In hóa đơn ra màn hình"""
        print("-" * 30)
        print(f"HÓA ĐƠN BÁN HÀNG")
        print(f"Khách hàng: {self.customer_name}")
        print(f"Ngày: {self.date}")
        print("-" * 30)
        
        for item in self.items:
            line_total = item['price'] * item['quantity']
            print(f"{item['name']:<15} x{item['quantity']:<3} {line_total:>10,.0f} VNĐ")
        
        print("-" * 30)
        print(f"TỔNG CỘNG: {self.calculate_total():>18,.0f} VNĐ")
        print("-" * 30)

# --- Chạy thử chương trình ---
if __name__ == "__main__":
    # Danh sách mặt hàng mẫu
    cart = [
        {'name': 'Sữa', 'price': 25000, 'quantity': 2},
        {'name': 'Bánh mì', 'price': 15000, 'quantity': 5},
        {'name': 'Trứng', 'price': 4000, 'quantity': 10}
    ]
    
    # Tạo và in hóa đơn
    my_invoice = Invoice("Nguyễn Văn A", cart)
    my_invoice.display_invoice()
    
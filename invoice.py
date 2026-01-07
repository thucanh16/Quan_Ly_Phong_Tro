import datetime
from config import INVOICES_FILE, INVOICE_UNPAID
from data_handler import load_data, save_data

class Invoice:
    def __init__(self, room_number, customer_name, items):
        self.room_number = room_number
        self.customer_name = customer_name
        self.items = items # [{name, price, quantity}]
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def save_to_db(self):
        invoices = load_data(INVOICES_FILE)
        new_data = {
            "room_number": self.room_number,
            "customer": self.customer_name,
            "date": self.date,
            "total": self.calculate_total(),
            "status": INVOICE_UNPAID
        }
        invoices.append(new_data)
        save_data(INVOICES_FILE, invoices)
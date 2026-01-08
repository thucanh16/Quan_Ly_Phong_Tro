import os

DATA_DIR = "data"
# File này lưu toàn bộ lịch sử để tính doanh thu (Chức năng 6 & 7)
INVOICES_FILE = os.path.join(DATA_DIR, "invoices.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
import tkinter as tk
from tkinter import messagebox
import invoice  # Gọi file invoice.py để dùng hàm create_invoice

def handle_calculate():
    # Lấy dữ liệu từ các ô nhập liệu
    r_id = entry_room.get()
    old = entry_old.get()
    new = entry_new.get()

    # Kiểm tra xem Mỹ Vân có quên nhập ô nào không
    if not r_id or not old or not new:
        messagebox.showwarning("Nhắc nhở", "Mỹ Vân hãy nhập đủ Mã phòng, Số cũ và Số mới nhé!")
        return

    try:
        # Chuyển số cũ và mới sang kiểu số nguyên
        old_val = int(old)
        new_val = int(new)

        if new_val < old_val:
            messagebox.showerror("Lỗi", "Số điện mới không được nhỏ hơn số cũ!")
            return

        # Gọi hàm từ file invoice.py của bạn để tính tiền và xuất file
        invoice.create_invoice(r_id, new_val, old_val)
        messagebox.showinfo("Thành công", f"Đã tính xong tiền phòng {r_id} và xuất hóa đơn thành công!")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số vào ô Chỉ số điện!")
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Có lỗi xảy ra: {e}")

# Thiết lập cửa sổ giao diện
app = tk.Tk()
app.title("Quản lý Phòng trọ - Mỹ Vân & Thục Anh")
app.geometry("400x400")

# Tiêu đề
tk.Label(app, text="HỆ THỐNG QUẢN LÝ PHÒNG TRỌ", font=("Arial", 14, "bold"), fg="#2c3e50").pack(pady=20)

# Các trường nhập liệu
tk.Label(app, text="Mã số phòng:").pack(pady=2)
entry_room = tk.Entry(app, width=30)
entry_room.pack(pady=5)

tk.Label(app, text="Chỉ số điện cũ:").pack(pady=2)
entry_old = tk.Entry(app, width=30)
entry_old.pack(pady=5)

tk.Label(app, text="Chỉ số điện mới:").pack(pady=2)
entry_new = tk.Entry(app, width=30)
entry_new.pack(pady=5)

# Nút bấm tính tiền
btn_calc = tk.Button(app, text="TÍNH TIỀN & XUẤT HÓA ĐƠN", command=handle_calculate, 
                     bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
btn_calc.pack(pady=30)

app.mainloop()

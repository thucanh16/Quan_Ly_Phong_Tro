import tkinter as tk
from tkinter import messagebox
from invoice import create_invoice

def tinh_tien():
    room_id = entry_room.get()
    dien_cu = entry_cu.get()
    dien_moi = entry_moi.get()

    if not room_id or not dien_cu or not dien_moi:
        messagebox.showwarning("Chú ý", "Mỹ Vân ơi, bạn hãy nhập đủ thông tin nhé!")
        return

    try:
        # Chuyển dữ liệu sang số và gọi hàm tính tiền từ invoice.py
        create_invoice(room_id, int(dien_moi), int(dien_cu))
        messagebox.showinfo("Thành công", f"Đã tính xong phòng {room_id} và xuất hóa đơn!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm Quản lý Phòng trọ - Mỹ Vân & Thục Anh")
root.geometry("400x300")

# Các ô nhập liệu trên giao diện
tk.Label(root, text="QUẢN LÝ PHÒNG TRỌ", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Mã số phòng:").pack()
entry_room = tk.Entry(root)
entry_room.pack()

tk.Label(root, text="Chỉ số điện cũ:").pack()
entry_cu = tk.Entry(root)
entry_cu.pack()

tk.Label(root, text="Chỉ số điện mới:").pack()
entry_moi = tk.Entry(root)
entry_moi.pack()

# Nút bấm tính tiền
btn_tinh = tk.Button(root, text="TÍNH TIỀN & XUẤT HÓA ĐƠN", command=tinh_tien, bg="green", fg="white", font=("Arial", 10, "bold"))
btn_tinh.pack(pady=20)

root.mainloop()
from data_handler import load_data, save_data

ROOM_PATH = "data/rooms.json"
TENANT_PATH = "data/tenants.json"
INVOICE_PATH = "data/invoices.json"

def create_invoice(room_id):
    rooms = load_data(ROOM_PATH)
    tenants = load_data(TENANT_PATH)
    invoices = load_data(INVOICE_PATH)

    # 1. Check if the room exist or not
    room = next((r for r in rooms if r["id"] == room_id), None)
    if room is None:
        print("The room doesn't exist!")
        return

    # 2. The room exist, then check if anyone is allocated for that room
    tenant = next((t for t in tenants if t["room_id"] == room_id), None)
    if tenant is None:
        print("No one is allocated for this room, can't create an invoice !")
        return

    # 3. Get amount from room.price
    amount = room["price"]

    # 4. Create invoice
    invoices.append({
        "room_id": room_id,
        "tenant": tenant["name"],
        "amount": amount
    })

    save_data(INVOICE_PATH, invoices)
    print(f"Create an invoice for the room {room_id} with price {amount} VNĐ — Tenant: {tenant['name']}")

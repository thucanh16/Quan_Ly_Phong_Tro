from data_handler import load_data, save_data

DATA_PATH = "data/rooms.json"

# This function is used for viewing the room list
def list_rooms():
    return load_data(DATA_PATH)

def add_room(room_id, price):
    # TO DO: Need to check the price must be a currency
    rooms = load_data(DATA_PATH)
    rooms.append({"id": room_id, "price": price})
    save_data(DATA_PATH, rooms)

def find_room(room_id):
    rooms = load_data(DATA_PATH)
    for r in rooms:
        if r["id"] == room_id:
            return print(f"There is that room: id {r["id"]}, price {r["price"]}")
    return print("The room doesn't exist")

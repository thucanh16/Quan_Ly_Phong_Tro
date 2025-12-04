from data_handler import load_data, save_data

DATA_PATH = "data/tenants.json"

def list_tenants():
    return load_data(DATA_PATH)

def add_tenant(name, room_id):
    tenants = load_data(DATA_PATH)
    tenants.append({"name": name, "room_id": room_id})
    save_data(DATA_PATH, tenants)

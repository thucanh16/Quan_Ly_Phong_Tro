import room
import tenant
import invoice

def main_menu():
    print("\n\n\t\t\t === Apartment Management ===")
    print("\t\t\t\t1. View a room list")
    print("\t\t\t\t2. Add a room")
    print("\t\t\t\t3. Add a tenant")
    print("\t\t\t\t4. Create invoice")
    print("\t\t\t\t5. Find room")
    print("\t\t\t\t0. Exit")
    print("\t\t\t === === === === === === ===\n\n")

while True:
    main_menu()
    choice = input("\tChoose: ")

    if choice == "1":
        print("[Result]: The room list is as follows: ")
        print(room.list_rooms())

    elif choice == "2":
        rid = input("Enter apartment's code: ")
        price = input("Enter apartment's price: ")
        room.add_room(rid, price)
        print("[LOG_INFO]: Added room")


    elif choice == "3":
        name = input("Enter tenant's name: ")
        rid = input("Enter apartment's code: ")
        tenant.add_tenant(name, rid)
        print("[LOG_INFO]: Added tenant")

    elif choice == "4":
        rid = input("Apartment's code: ")
        invoice.create_invoice(rid)

    elif choice == "5":
        rid = input("Apartment's code: ")
        room.find_room(rid)

    elif choice == "0":
        break

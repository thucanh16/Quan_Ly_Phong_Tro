import room
import tenant
import invoice


def main_menu():
    print("\n====== APARTMENT MANAGEMENT ======")
    print("1. View room list")
    
    print("2. Add a room")
    print("3. Add a tenant")
    print("4. Create invoice")
    print("5. Find room")
    print("0. Exit")
    print("=================================")


def main():
    while True:
        main_menu()
        choice = input("Choose: ")

        if choice == "1":
            rooms = room.list_rooms()
            print("\n--- ROOM LIST ---")
            for r in rooms:
                print(r)

        elif choice == "2":
            rid = input("Enter room ID: ")
            try:
                price = int(input("Enter room price: "))
                room.add_room(rid, price)
                print("[SUCCESS] Room added.")
            except ValueError:
                print("[ERROR] Price must be a number!")

        elif choice == "3":
            name = input("Enter tenant name: ")
            rid = input("Enter room ID: ")
            tenant.add_tenant(name, rid)
            print("[SUCCESS] Tenant added.")

        elif choice == "4":
            rid = input("Enter room ID: ")
            invoice.create_invoice(rid)
            print("[SUCCESS] Invoice created.")

        elif choice == "5":
            rid = input("Enter room ID: ")
            result = room.find_room(rid)
            if result:
                print(result)
            else:
                print("[INFO] Room not found.")

        elif choice == "0":
            print("Exit program.")
            break

        else:
            print("[ERROR] Invalid choice!")


if __name__ == "__main__":
    main()

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            print(f"{name} exists. Use option 2 to update.")
        else:
            self.items[name] = quantity
            print(f"Added {name} with quantity {quantity}")

    def update_item(self, name, quantity):
        if name in self.items:
            self.items[name] = quantity
            print(f"Updated {name} to quantity {quantity}")
        else:
            print(f"{name} not found. Use option 1 to add.")

    def get_item(self, name):
        print(f"{name}: {self.items.get(name, 'Not found')}")

    def show_summary(self):
        print(f"Total unique items: {len(self.items)}")
        print(f"Total quantity of all items: {sum(self.items.values())}")


inventory = Inventory()

while True:
    print("\n1. Add Item  2. Update Item  3. Retrieve Item  4. Summary  5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        inventory.add_item(input("Item name: "), int(input("Quantity: ")))
    elif choice == "2":
        inventory.update_item(input("Item name: "), int(input("New quantity: ")))
    elif choice == "3":
        inventory.get_item(input("Item name: "))
    elif choice == "4":
        inventory.show_summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

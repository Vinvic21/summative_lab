import requests

base_url ="http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{base_url}/inventory")
    print(response.json())

def view_inventory_by_id():
    barcode = input("enter barcode: ")
    response = requests.get(f"{base_url}/inventory/{barcode}")
    print(response.json())

def add_item():
    barcode = input("enter barcode: ")
    response = requests.post(f"{base_url}/inventory", json={"barcode": barcode})
    try:
        print(response.json())
    except ValueError:
        print("error")

def update_item():
    barcode = input("enter barcode: ")
    item = input("enter item to edit eg price: ")
    value = input("enter the value to be changed:")
    if item in ["price", "stock"]:
        value = float(value) if item == "price" else int(value)
    else:
        raise ValueError("invalid input")
    response = requests.patch(f"{base_url}/inventory/{barcode}", json={item: value})
    print(response.json())

def delete_item():
    barcode = input("enter barcode: ")
    response = requests.delete(f"{base_url}/inventory/{barcode}")
    print("Item deleted")
    
def cli_command():
    while True:
        print("Inventory CLI")
        print("1. View inventory Items: ")
        print("2. View Specific item: ")
        print("3. Add Item to the inventory: ")
        print("4. Update Item: ")
        print("5. Delete Item: ")
        print("6. Exoit: ")
        choice  = input("Choose an option: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            view_inventory_by_id()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == ("__main__"):
    cli_command()
# Food Menu Management System 
# A simple system to manage food menu items and orders

menu_items = {'sushi':       {'name': 'Sushi', 'price': 350, 'category': 'Japanese'},
    'tacos':       {'name': 'Tacos', 'price': 180, 'category': 'Mexican'},
    'paella':      {'name': 'Paella', 'price': 420, 'category': 'Spanish'},
    'lasagna':     {'name': 'Lasagna', 'price': 280, 'category': 'Italian'},
    'falafel':     {'name': 'Falafel', 'price': 150, 'category': 'Middle Eastern'},
    'poutine':     {'name': 'Poutine', 'price': 200, 'category': 'Canadian'},
    'dim_sum':     {'name': 'Dim Sum', 'price': 190, 'category': 'Chinese'},
    'churros':     {'name': 'Churros', 'price': 130, 'category': 'Dessert'},
    'bibimbap':    {'name': 'Bibimbap', 'price': 320, 'category': 'Korean'},
    'baklava':     {'name': 'Baklava', 'price': 140, 'category': 'Turkish Dessert'},
    'ceviche':     {'name': 'Ceviche', 'price': 270, 'category': 'Peruvian'},
    'moussaka':    {'name': 'Moussaka', 'price': 310, 'category': 'Greek'},
    'pierogi':     {'name': 'Pierogi', 'price': 160, 'category': 'Polish'},
    'ramen':       {'name': 'Ramen', 'price': 260, 'category': 'Japanese'},
    'empanadas':   {'name': 'Empanadas', 'price': 170, 'category': 'Argentinian'},}

orders_list = []


def display_menu():
    """Display all available food items with their prices and categories."""
    print("\n" + "="*60)
    print("WELCOME TO INDIAN FOOD MENU MANAGEMENT SYSTEM")
    print("="*60)
    print("\nAvailable Food Items:\n")
    
    for item_id, details in menu_items.items():
        print(f"{item_id.upper():20} | Price: ₹{details['price']:4} | Category: {details['category']}")
    
    print("="*60 + "\n")


def add_food_item(item_id, name, price, category):
    """Add a new food item to the menu."""
    if item_id in menu_items:
        print(f"Error: Item '{item_id}' already exists in menu.")
        return False
    
    menu_items[item_id] = {'name': name,
        'price': price,
        'category': category}
    print(f"Successfully added '{name}' to menu at ₹{price}")
    return True


def remove_food_item(item_id):
    """Remove a food item from the menu."""
    if item_id not in menu_items:
        print(f"Error: Item '{item_id}' not found in menu.")
        return False
    
    removed_item = menu_items.pop(item_id)
    print(f"Successfully removed '{removed_item['name']}' from menu.")
    return True


def update_food_price(item_id, new_price):
    """Update the price of an existing food item."""
    if item_id not in menu_items:
        print(f"Error: Item '{item_id}' not found in menu.")
        return False
    
    old_price = menu_items[item_id]['price']
    menu_items[item_id]['price'] = new_price
    print(f"Updated price for '{menu_items[item_id]['name']}' from ₹{old_price} to ₹{new_price}")
    return True


def place_order(item_id, quantity):
    """Place an order for a food item with specified quantity."""
    if item_id not in menu_items:
        print(f"Error: Item '{item_id}' not found in menu.")
        return False
    
    if quantity <= 0:
        print("Error: Quantity must be greater than 0.")
        return False
    
    item = menu_items[item_id]
    total_price = item['price'] * quantity
    
    order = {
        'item_id': item_id,
        'item_name': item['name'],
        'quantity': quantity,
        'unit_price': item['price'],
        'total_price': total_price
    }
    
    orders_list.append(order)
    print(f"Order placed: {quantity}x {item['name']} = ₹{total_price}")
    return True


def view_current_orders():
    """Display all current orders with details."""
    if not orders_list:
        print("\nNo orders placed yet.\n")
        return
    
    print("\n" + "="*70)
    print("CURRENT ORDERS")
    print("="*70)
    
    total_amount = 0
    for index, order in enumerate(orders_list, 1):
        print(f"{index}. {order['item_name']} x{order['quantity']} ₹{order['unit_price']} = ₹{order['total_price']}")
        total_amount += order['total_price']
    
    print("-"*70)
    print(f"Total Bill Amount: ₹{total_amount}")
    print("="*70 + "\n")
    
    return total_amount


def calculate_bill():
    """Calculate the total bill amount for all current orders."""
    if not orders_list:
        print("No orders to calculate bill for.")
        return 0
    
    total = sum(order['total_price'] for order in orders_list)
    return total


def clear_all_orders():
    """Clear all orders from the order list."""
    if not orders_list:
        print("No orders to clear.")
        return False
    
    orders_list.clear()
    print("All orders have been cleared.")
    return True


def search_food_by_category(category):
    """Search for food items by category."""
    items_found = [item for item_id, item in menu_items.items() 
                   if item['category'] == category]
    
    if not items_found:
        print(f"No items found in category '{category}'.")
        return []
    
    print(f"\nItems in category '{category}':")
    for item in items_found:
        print(f"  - {item['name']}: ₹{item['price']}")
    
    return items_found


def get_menu_statistics():
    """Get statistics about the menu and orders."""
    print("\n" + "="*50)
    print("MENU STATISTICS")
    print("="*50)
    print(f"Total items in menu: {len(menu_items)}")
    print(f"Total orders placed: {len(orders_list)}")
    
    if orders_list:
        total_bill = calculate_bill()
        avg_order_value = total_bill / len(orders_list)
        print(f"Total bill amount: ₹{total_bill}")
        print(f"Average order value: ₹{avg_order_value:.2f}")
    
    categories = set(item['category'] for item in menu_items.values())
    print(f"Total categories: {len(categories)}")
    print("="*50 + "\n")


def main_menu():
    """Main menu loop for user interaction."""
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Display Menu")
        print("2. Place Order")
        print("3. View Current Orders")
        print("4. View Bill")
        print("5. Search by Category")
        print("6. Add New Item (Admin)")
        print("7. Remove Item (Admin)")
        print("8. Update Price (Admin)")
        print("9. Clear All Orders")
        print("10. View Statistics")
        print("11. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-11): ").strip()
        
        if choice == '1':
            display_menu()
        
        elif choice == '2':
            display_menu()
            item_id = input("Enter item ID: ").strip().lower()
            try:
                quantity = int(input("Enter quantity: ").strip())
                place_order(item_id, quantity)
            except ValueError:
                print("Error: Please enter a valid number for quantity.")
        
        elif choice == '3':
            view_current_orders()
        
        elif choice == '4':
            total = calculate_bill()
            print(f"Total Bill: ₹{total}\n")
        
        elif choice == '5':
            category = input("Enter category name: ").strip().lower()
            search_food_by_category(category)
        
        elif choice == '6':                                                 
            item_id = input("Enter item ID: ").strip().lower()
            name = input("Enter item name: ").strip()
            try:
                price = int(input("Enter price (in rupees): ").strip())
                category = input("Enter category: ").strip().lower()
                add_food_item(item_id, name, price, category)
            except ValueError:
                print("Error: Please enter a valid price.")
        
        elif choice == '7':
            item_id = input("Enter item ID to remove: ").strip().lower()
            remove_food_item(item_id)
        
        elif choice == '8':
            item_id = input("Enter item ID: ").strip().lower()
            try:
                new_price = int(input("Enter new price (in rupees): ").strip())
                update_food_price(item_id, new_price)
            except ValueError:
                print("Error: Please enter a valid price.")
        
        elif choice == '9':
            confirm = input("Are you sure? This will clear all orders (yes/no): ").strip().lower()
            if confirm == 'yes':
                clear_all_orders()
        
        elif choice == '10':
            get_menu_statistics()
        
        elif choice == '11':
            print("\nThank you for using Food Menu Management System!")
            print("See you soon!\n")
            break

        else:
            print("Error: Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()

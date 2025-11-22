# 🍲Food Menu Management System 

A simple, Command-Line-Based python script for managing a food menu and handling customer orders. This system allows for displaying menu items, placing orders, calculating bills and performing basic administrative tasks like adding, removing and updating food items 

## ✨ Features 
**Menu Display:** View all available food items, their prices, and their categories.
**Order Management:** Place new orders and veiw all current, pending orders.
**Billing:** Calculate the total bill for all placed orders.
**Menu Adminstrative(Admin):**
   * Add new food items to the menu.
   * Remove existing food items.
   * Update the price of any menu item.
**Search Functionality:** Search For menu items based on their category.
**Statistics:** Veiw quick statistics on the total number of menu items, orders placed, and average order value.

## 🚀 Getting Started 

### Prerequisites 

This is a Python script and requires **Python 3.x** to run.

##💻Usage 

The system runs in a continous loop, presenting a main menu with 11 options. To interact, Simply enter teh number corresponding to the action you wish to perform.
| Choice | Action | Description | Access |
| :----: | :---------------------- | :--------------------------------------------- | :----: |
| 1 | **Display Menu** | Shows the full list of available food items. | All |
| 2 | **Place Order** | Prompts for an item ID and quantity to add an order. | All |
| 3 | **View Current Orders** | Displays a detailed list of all pending orders. | All |
| 4 | **View Bill** | Calculates and shows the total bill amount. | All |
| 5 | **Search by Category** | Finds items belonging to a specified category. | All |
| 6 | **Add New Item** | *Admin action:* Adds a new food item to the `menu_items` dictionary. | Admin |
| 7 | **Remove Item** | *Admin action:* Deletes an item from the menu by ID. | Admin |
| 8 | **Update Price** | *Admin action:* Changes the price of an existing item. | Admin |
| 9 | **Clear All Orders** | Clears the entire `orders_list`. Requires confirmation. | All |
| 10 | **View Statistics** | Displays general menu and order metrics. | All |
| 11 | **Exit** | Closes the application. | All |

##📁Project Structure 

the Entire Application is contained within a single Python file.

* `Food Menu Mangement system.py` - The core script containing all functions and the main menu loop.
    * **Data Structures:**
        *`menu_items`: A dictionary storing food items, keyed by a unique item ID (e.g.`Sushi`).
        *`orders_list`: A list used to store Dictionaries representing placed order.
    * **Functions:** Contains helper function drives the application's user interface.

##💡Future Enhancemets 

* **Persistence:** Save menu and Data to a file (CSV, JSON or a simple database) so the data persists after the script is closed.
* **Admin Login** Implement a simple password or token system to secure the administrative functions (options 6,7,8).
* **Order Fulfillment:** Add functionality to mark orders as "Completed" and move them to a history log.
* **Error Handling:** Improve robustness with more Detailed input validation.
* **GUI:** Convert teh command-line interface to a Graphical User Interface (GUI) using libraries like Tkinter or PyQt.

##🤝Contributing 

Contributing are welcome! If you have suggestions for improvement, please open an issue or submit a pull request.

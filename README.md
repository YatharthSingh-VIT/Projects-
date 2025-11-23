**🍛Food Menu System**

 Customers' orders in this fast food restaurant service system can also be handled by Python-based programs that run a few basic food menu items.  It offers the ability to print menu items, place orders, compute the amount owed, and perform a few administrative tasks like adding or removing items from the menu.

 **✨Special points**

 **Menu display: +  View all of the food items that are available, along with their corresponding costs and categories.

 **Order management: + Place new orders and review all existing ones.

 **Billing:+ Determine the total amount owed for each order placed so far.

**Menu Administrative (Admin)** -- Requirements  Include new meals on the menu.  --* Remove any dish you choose.  --* Modify a food item's price.
 **Search Functionality:** Look for menu items by category.
 **Statistics:  View brief data on the average order value, the total amount of menu items, and the number of orders placed.

 ## Getting Started 

 ### Requirements 

 To run this, the Python script **Python 3.x** is needed.

 ## Usage 

 The system displays an 11-option primary menu while operating in a continuous loop.  To engage, just input the number that corresponds to the desired action.
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

##📁Project Organization 

 One Python file contains the complete application.

 * `Food Menu Mangement system.py`: All functions and the primary menu loops are contained in this core script.
     * **Data Structures:** *`menu_items`: A dictionary with food items stored, each keyed by a distinct item ID (e.g., `Sushi`).
         * Dictionaries that represent placed orders are stored in a list called `orders_list`. * Functions:  The application's user interface is driven by a helper function.

 ## Future Improvements 

 * **Persistence:** To ensure that the data remains when the script is closed, save the menu and data to a file (CSV, JSON, or a basic database).
 * **Admin Login** To safeguard administrative operations, use a straightforward password or token system (options 6,7,8).
 * Order fulfillment: Provide the ability to mark orders as "Completed" and transfer them to the history log.
 * Error Handling: Enhance resilience through thorough input verification.
* **GUI:** Convert teh command-line interface to Graphical User Interface (GUI) using libraries like Tkinter or PyQt.

##🤝Contributing 

Contributing are welcome! If you have suggestions for improvement, please open an issue or submit a pull request.


*Aurthor - Yatharth Singh* 

*Reg No - 25BAI10657*

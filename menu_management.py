# Program: Restaurant Menu Updater

def add_dish(menu_list, new_dish):
    """Adds a new dish to menu."""
    menu_list.append(new_dish)
    return menu_list

def delete_dish(menu_list, dish_name):
    """Removes a dish if present."""
    if dish_name in menu_list:
        menu_list.remove(dish_name)
    else:
        print(f"'{dish_name}' is not in the menu!")
    return menu_list

def is_available(menu_list, dish_name):
    """Checks if a dish is available in the menu."""
    return f"Yes, {dish_name} is available" if dish_name in menu_list else f"No, {dish_name} not found"

# Example run
menu = ["Pizza", "Burger", "Pasta", "Salad"]
menu = add_dish(menu, "Tacos")
menu = delete_dish(menu, "Salad")
print("Updated Menu:", menu)
print(is_available(menu, "Pizza"))

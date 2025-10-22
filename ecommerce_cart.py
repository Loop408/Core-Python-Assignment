# Program: E-Commerce Cart Billing System

def get_bill(cart):
    """Return final amount after discount if applicable."""
    if len(cart) == 0:
        return "Your shopping cart is empty!"
    
    amount = sum(cart.values())
    if len(cart) > 5:
        discount = 0.10 * amount
        amount -= discount
    return amount

# Example run
cart = {"Laptop": 50000, "Headphones": 2000, "Mouse": 500, "Keyboard": 1500}
final_amount = get_bill(cart)
print(f"Total payable amount: ₹{int(final_amount)}")

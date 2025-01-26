# Function to calculate discount
def calculate_discount(price):
    if price > 5000:
        return price * 0.10  # 10% discount
    elif price > 1000:
        return price * 0.05  # 5% discount
    else:
        return 0  # No discount for prices <= 1000

try:
    price = float(input("Enter the total price of goods: "))

    discount = calculate_discount(price)
    final_price = price - discount

    print(f"Discount: {discount:.2f}")
    print(f"Final price to pay: {final_price:.2f}")
except ValueError:
    print("Please enter a valid number for the price.")

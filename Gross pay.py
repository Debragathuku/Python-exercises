# Function to calculate gross pay
def calculate_gross_pay(rate, hours_worked):
    return rate * hours_worked

try:
    rate = float(input("Enter your hourly rate: "))
    hours_worked = float(input("Enter the number of hours worked: "))

    gross_pay = calculate_gross_pay(rate, hours_worked)

    print(f"Your gross pay is: {gross_pay:.2f}")
except ValueError:
    print("Please enter valid numerical values for rate and hours worked.")

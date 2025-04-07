# Electricity Bill Calculator

# Prompt the user to enter details
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = float(input("Enter Units Consumed: "))

# Determine charges per unit based on units consumed
if units_consumed <= 199:
    charges_per_unit = 1.20
elif 200 <= units_consumed < 400:
    charges_per_unit = 1.50
elif 400 <= units_consumed < 600:
    charges_per_unit = 1.80
else:
    charges_per_unit = 2.00

# Calculate the total bill
total_bill = units_consumed * charges_per_unit

# Apply surcharge if the bill exceeds Kshs. 400
if total_bill > 400:
    surcharge = total_bill * 0.15  # 15% surcharge
    total_bill += surcharge

# Ensure the minimum bill is Kshs. 100
if total_bill < 100:
    total_bill = 100

# Display the bill details
print("\nElectricity Bill")
print(f"Customer ID      : {customer_id}")
print(f"Customer Name    : {customer_name}")
print(f"Units Consumed   : {units_consumed}")
print(f"Charges per Unit : Ksh {charges_per_unit:.2f}")
print(f"Total Amount to Pay: Ksh {total_bill:.2f}")

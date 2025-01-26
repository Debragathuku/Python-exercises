# Function to check divisibility by 11
def is_divisible_by_11(number):
    if number % 11 == 0:
        return True
    else:
        return False
 
try:
    number = int(input("Enter a number to check divisibility by 11: "))
    
    if is_divisible_by_11(number):
        print(f"{number} is divisible by 11.")
    else:
        print(f"{number} is not divisible by 11.")
except ValueError:
    print("Please enter a valid integer!")

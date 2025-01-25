import math

def calculate_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    Formula: Volume = (4/3) * π * r^3
    """
    return (4/3) * math.pi * (radius ** 3)

try:
    radius = float(input("Enter the radius of the sphere: "))
    
    volume = calculate_volume(radius)
    
    print(f"The volume of the sphere is: {volume:.2f}")

except ValueError:
    print("Invalid input! Please enter a numeric value for the radius.")

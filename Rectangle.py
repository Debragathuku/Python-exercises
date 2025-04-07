class Rectangle:
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create a Rectangle object with user input
rect = Rectangle(length, width)

# Compute and display area and perimeter
print(f"\nRectangle Details:")
print(f"Length     : {rect.length}")
print(f"Width      : {rect.width}")
print(f"Area       : {rect.area()}")
print(f"Perimeter  : {rect.perimeter()}")

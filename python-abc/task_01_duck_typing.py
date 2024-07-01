from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height."""
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Example usage:
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    print("Circle:")
    shape_info(circle)  # Should print the area and perimeter of the circle

    print("\nRectangle:")
    shape_info(rectangle)  # Should print the area and perimeter of the rectangle

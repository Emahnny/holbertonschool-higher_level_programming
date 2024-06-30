from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass

class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius.

        Args:
            radius (float): The radius of the circle. If negative, set to 0.
        """
        self.radius = max(0, radius)  # Ensure radius is non-negative

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

def shape_info(shape):
    """Print the area and perimeter of a shape.

    Args:
        shape (Shape): An object that has area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Example usage:
if __name__ == "__main__":
    circle = Circle(5)
    circle_negative = Circle(-5)  # Should set radius to 0 automatically

    print("Circle:")
    shape_info(circle)  # Should print the area and perimeter of the circle

    print("\nNegative Circle:")
    shape_info(circle_negative)  # Should print the area and perimeter of the circle with radius 0

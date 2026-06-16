import math

class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"{self.name}(width={self.width},height = {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(5,3)
circle = Circle(4)

print(rect)
print(f"Area: {rect.area():.2f}")

print(f"\nCircle(radius={circle.radius})")
print(f"Area: {circle.area():.2f}")

        
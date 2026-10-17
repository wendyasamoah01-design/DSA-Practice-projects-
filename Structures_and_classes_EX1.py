#Using structures to create a data record for shapes, your program should return the area of the following shapes:
# 1. Rectangle
# 2. Circle
# 3. Cuboid
# 4. Triangle

class Shapes:
    def __init__(self):
        pass

    def rectangle_area(self, length, width):
        return length * width

    def circle_area(self, radius):
        import math
        return math.pi * (radius ** 2)

    def cuboid_area(self, length, width, height):
        return 2 * (length * width + length * height + width * height)

    def triangle_area(self, base, height):
        return 0.5 * base * height
    
    
print("Here are the available shapes:")
print("1. Rectangle")  
print("2. Circle")
print("3. Cuboid")
print("4. Triangle")

Choice = int(input("Enter the number corresponding to the shape you want to calculate the area for: "))

if Choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    shape = Shapes()
    area = shape.rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
    
elif Choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    shape = Shapes()
    area = shape.circle_area(radius)
    print(f"The area of the circle is: {area}")
    
elif Choice == 3:
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    shape = Shapes()
    area = shape.cuboid_area(length, width, height)
    print(f"The surface area of the cuboid is: {area}")
    
elif Choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    shape = Shapes()
    area = shape.triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
    
else:
    print("Invalid choice. Please select a number between 1 and 4.")    

  
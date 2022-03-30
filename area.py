# Create a  menu-driven python program “ area.py “ with the following menu
#
# 1. calculate the area of rectangle
# 2. perimeter of a rectangle
# 3. area of circle
# 4. Area of square
# 5. Area of a triangle
#
# After completing the above program, write test-cases for the operations by using Pytest

def area_of_rectangle(length, breadth):
    return length * breadth

def perimeter_of_rectangle(length, breadth):
    return 2*(length + breadth)

def area_of_circle(radius):
    return 3.14*radius*radius

def area_of_square(side):
    return side * side

def area_of_triangle(breadth, height):
    return 1/2*(breadth * height)

if __name__ == "__main__":
    while True:
        print("1.Area of Rectangle")
        print("2.Perimeter of Rectangle")
        print("3.Area of Circle")
        print("4.Area of Square")
        print("5.Area of Triangle")
        print("6. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            length = int(input("Enter length of a rectangle:"))
            breadth = int(input("Enter length of a breadth:"))
            areaOfRectangle = area_of_rectangle(length, breadth)
            print(areaOfRectangle)

        elif choice == 2:
            length = int(input("Enter length of a rectangle:"))
            breadth = int(input("Enter breadth of a rectangle:"))
            perimeterOfRectangle = perimeter_of_rectangle(length, breadth)
            print(perimeterOfRectangle)

        elif choice == 3:
            radius = int(input("Enter radius of a circle:"))
            areaOfCircle = area_of_circle(radius)
            print(areaOfCircle)

        elif choice == 4:
            side = int(input("Enter side of a square:"))
            areaOfSquare = area_of_square(side)
            print(areaOfSquare)

        elif choice == 5:
            breadth = int(input("Enter breadth of a triangle:"))
            height = int(input("Enter height of a triangle:"))
            areaOfTriangle = area_of_triangle(breadth, height)
            print(areaOfTriangle)

        elif choice ==6:
            break
        else:
            print("invalid choice")






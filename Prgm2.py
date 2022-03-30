# Write a Python program to find the
# Surface area, volume and space diagonal of rectangular
# prism by reading the length breadth and height of the prism from the user. Also write the test-case for the functions by using pytest .

def area(length, width, height):
    return 2*((width*length)+(height*length)+(height*width))

def volume(length, width, height):
    return length*width*height

def spaceDiagonal(length, width, height):
    diagonal = ((length*length) + (width*width) + (height*height))
    sqrt = diagonal ** 0.5
    return sqrt

if __name__ == "__main__":
    length = int(input("Enter length:"))
    breadth = int(input("Enter breadth:"))
    height = int(input("Enter height:"))

    result = area(length, breadth, height)
    print(result)

    result = volume(length, breadth, height)
    print(result)

    result = spaceDiagonal(length, breadth, height)
    print(result)




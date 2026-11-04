l=float(input("Enter the legth of the rectangle : "))
b=float(input("Enter the breadth of the rectangle : "))
rectangle = lambda l,b:l*b
print("Area of Rectangle is ",rectangle(l,b))

h=float(input("Enter the height of the triangle : "))
b=float(input("Enter the breadth of the triangle : "))
triangle = lambda h,b:1/2*h*b
print("Area of triangle is ",triangle(h,b))

side=float(input("Enter the legth of side of square : "))
square = lambda side:side*side
print("Area of square is ",square(side))

def area_square():
    s=eval(input("Enter side: "))
    area=s*s
    print("The area of the square is {}".format(area))

def area_rectangle():
    l=eval(input("Enter length: "))
    b=eval(input("Enter breadth: "))
    area=l*b
    print("The area of the rectangle is {}".format(area))

def area_circle():
    r=eval(input("Enter radius: "))
    area=3.14*r*r
    print("The area of the circle is {}".format(area))
#Driver code
if __name__=='__main__':
    area_square()
    area_rectangle()
    area_circle()
    print("The name of the function is",__name__)


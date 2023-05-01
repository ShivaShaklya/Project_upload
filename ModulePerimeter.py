def p_rectangle():
    l=eval(input("Enter Length: "))
    b=eval(input("Enter Breadth: "))
    p=2*(l+b)
    print("The primeter of the rectangle is {}".format(p))

def p_square():
    s=eval(input("Enter side: "))
    p=4*s
    print("The primeter of the square is {}".format(p))

def p_circle():
    r=eval(input("Enter radius"))
    p=2*3.14*r
    print("The primeter of the circle is {}".format(p))
    
#Driver code
if __name__=="__main__":
    p_square()
    p_rectangle()
    p_circle()
print("name of the function is",__name__)
